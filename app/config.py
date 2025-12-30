from flask_pymongo import PyMongo
import os
import certifi

mongo = PyMongo()

def init_db(app):
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    app.config["MONGO_TLS_CA_FILE"] = certifi.where()
    mongo.init_app(app)
