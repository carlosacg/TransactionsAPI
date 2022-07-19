from sqlalchemy.sql import functions, func
from models import User, Transaction, db
import os


def read_csv():
    import pandas as pd

    df = pd.read_csv("credit_debit_data.csv")
    return df


def create_or_get_user(email: str):
    db_user = User.query.filter(
        User.email == email).first()

    if db_user:
        return db_user.id

    user = User(email=email)
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)

    return user.id


def get_info_account(user_id: int):
    db_user = User.query.filter(
        User.id == user_id).first()
    total_balance = get_total_balance(user_id)
    total_credit = get_average_credit(user_id)
    total_debit = get_average_debit(user_id)
    transactions_by_month = get_quantity_transaction_by_month(user_id)
    message = """
        Dear {user_email} here is your summary of your data

        Total balance is {total_balance}
        Average debit amount: {total_debit}
        Average credit amount: {total_credit}

        Transactions by month
        {transactions_by_month}
    """.format(
        user_email=db_user.email,
        total_balance=total_balance,
        total_debit=total_debit,
        total_credit=total_credit,
        transactions_by_month=transactions_by_month
    )

    return message


def get_total_balance(user_id: int):
    query = db.select(
        [functions.sum(Transaction.amount)]
    ).filter(Transaction.owner_id == user_id)
    return round(db.session.execute(query).fetchall()[0][0], 2)


def get_average_credit(user_id: int):
    query = db.select(
        [func.avg(Transaction.amount)]
    ).filter(Transaction.owner_id == user_id, Transaction.amount > 0)
    return round(db.session.execute(query).fetchall()[0][0], 2)


def get_average_debit(user_id: int):
    query = db.select(
        [func.avg(Transaction.amount)]
    ).filter(Transaction.owner_id == user_id, Transaction.amount < 0)
    return round(db.session.execute(query).fetchall()[0][0], 2)


def get_quantity_transaction_by_month(user_id: int):
    import calendar

    data_transactions = Transaction.query.with_entities(Transaction.month, func.count(
        Transaction.id)).filter(Transaction.owner_id == user_id).group_by(Transaction.month).order_by(Transaction.month).all()
    message = ''
    for transaction in data_transactions:
        message += "Number of transaction in {}: {}\n\t".format(
            calendar.month_name[transaction[0]],
            transaction[1])
    return message


def send_email(receiver: str, subject_message: str, body_message: str):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    sender = os.environ.get('SENDER_EMAIL')
    sender_pass = os.environ.get('SENDER_KEY')

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject_message

    message.attach(MIMEText(body_message, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender, sender_pass)
    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()
