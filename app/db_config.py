from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "GB981UA7YT91"
engine = create_engine('mysql+pymysql://root:root@localhost:3306/kimia-is')
Session = sessionmaker(bind=engine)
sess = Session()

db = SQLAlchemy(app)