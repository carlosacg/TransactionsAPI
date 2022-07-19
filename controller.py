from app import app
from models import Transaction, db
from flask import request
from datetime import date, datetime
from fnutils import read_csv, create_or_get_user,  get_info_account, send_email


@app.route('/', methods=['GET'])
def hello():
    return "Welcome to Transaction API develop by carlosacg"


@app.route('/transactions/load_data', methods=['POST'])
def load_data():
    params = request.json
    user_email = params.get('email')
    user_id = create_or_get_user(user_email)
    df = read_csv()
    now = datetime.now()
    for i in df.index:
        month, day = df["Date"][i].split('/')
        transaction_date = date(now.year, int(month), int(day))
        transaction_amount = df["Transaction"][i]
        transaction_obj = Transaction(transaction_date, transaction_amount)
        transaction_obj.month = int(month)
        transaction_obj.owner_id = user_id
        db.session.add(transaction_obj)
        db.session.commit()
    message = get_info_account(user_id)
    send_email(user_email, "Summary account", message)
    return message
