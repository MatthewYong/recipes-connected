import os
from flask import Flask, render_template, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")


mongo = PyMongo(app)

@app.route('/')
def test():
    return 'Hello Test'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

