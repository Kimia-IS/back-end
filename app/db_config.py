from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = "GB981UA7YT91"
engine = create_engine('mysql+pymysql://root@localhost:3306/kimiais')
Session = sessionmaker(bind=engine)
sess = Session()

db = SQLAlchemy(app)
migrate = Migrate(app, db)