from logging import DEBUG
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{password}@{host}/{db}'.format(
    user=os.environ.get('USER_DB'),
    password=os.environ.get('PASSWORD_DB'),
    host=os.environ.get('HOST_DB'),
    db=os.environ.get('DB_NAME'),
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = SQLAlchemy(app) 

from controller import *

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run('0.0.0.0', 8084, debug=True)