import os
from flask import Flask
from flask_pymongo import PyMongo


def create_app():
    app = Flask(__name__)

    #app.config['MONGO_DBNAME'] = 'restdb'
    app.config['MONGO_URI'] = os.environ.get('DB')
    return app
