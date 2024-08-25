from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Python312/00Flask/FlaskMarket/market.db"
db = SQLAlchemy(app)

from market import routes



#end