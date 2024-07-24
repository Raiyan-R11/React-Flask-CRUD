#app config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 
#^cross origin request. want frontend to communicate with backend

app= Flask(__name__)
CORS(app)#disables errors


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
#local database on machine.
#///rel
#////abs 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

