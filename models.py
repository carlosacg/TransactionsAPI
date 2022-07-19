from app import db
from sqlalchemy.orm import backref, relationship


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, index=True)

    transactions = relationship("Transaction", backref="owner")


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    amount = db.Column(db.Float)
    month = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, date, amount):
        self.date = date
        self.amount = amount
