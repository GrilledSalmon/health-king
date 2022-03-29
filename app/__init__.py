from app.views.recruit_card_view import recruit_card
from flask import Flask, render_template, jsonify, request
from .views import login_view, signup_view, recruit_card_view
from bson.objectid import ObjectId

import requests

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.dbjungle

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/main', methods=['GET'])
def listing():

    result = list(db.health.find({}))

    for i in range(len(result)):
        temp_id = str(result[i]['_id']) 
        del result[i]['_id'] 
        result[i]['_id'] = temp_id 

    return jsonify({'result':'success', 'activities': result})



@app.route('/main/registration', methods=['POST'])
def posting():
    receive_acname = request.form['give_acname']
    receive_time = request.form['give_time']
    receive_place = request.form['give_place']
    receive_content = request.form['give_content']

    print("sadfefe",receive_acname, receive_time, receive_place, receive_content)

    doc = {
        'acname' : receive_acname,
        'time' : receive_time,
        'place' : receive_place,
        'content' : receive_content
        }

    db.health.insert_one(doc)

    print("doc:",doc)

    return jsonify({'result': 'success'})

# devsds
app.register_blueprint(login_view.bp)
app.register_blueprint(signup_view.bp)
app.register_blueprint(recruit_card_view.bp)
