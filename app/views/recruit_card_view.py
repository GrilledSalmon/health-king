from flask import Blueprint, render_template, jsonify, request
from bson.objectid import ObjectId
from app import card_collection
from app import user_collection

bp = Blueprint('recruit_card',__name__)

@bp.route('/recruit_card')
def recruit_card():
    return render_template('index.html')

@bp.route('/main', methods=['GET'])
def listing():

    result = list(card_collection.find({}))
    print(result)
    for i in range(len(result)):
        temp_id = str(result[i]['_id']) 
        del result[i]['_id'] 
        result[i]['_id'] = temp_id 

    return jsonify({'result':'success', 'activities': result})


@bp.route("/main/login", methods=['GET'])
def listing_login():

    userID = 'TEMPNAME2'

    user_ac = user_collection.find_one({'id':userID})

    result = []

    for activity in user_ac['activity']:
        print(activity)
        bson_id = ObjectId(activity)
        temp_dic = card_collection.find_one({'_id':bson_id}, {'_id': 0})
        result.append(temp_dic)
    
    print('-'*20)
    print(result)
    print('-'*20)

    return jsonify({'result':'success', 'activities': result})


@bp.route('/main/join', methods=['POST'])
def join():
    userID = 'TEMPNAME2'
    userName = 'TEMPID2'
    receive_oID = request.form['give_ID']
    print("total:", list(user_collection.find()))

    user_target = user_collection.find_one({'id':userID})

    print("usertaget:", user_target)
    user_target['activity'].append(receive_oID)

    target_user = user_target['activity']

    user_collection.update_one({'id':userID},{'$set':{'activity':target_user}})

    bson_id = ObjectId(receive_oID)

    target = card_collection.find_one({'_id':bson_id})

    if userName in target['participant']:
        return jsonify({'result': 'fail'})


    target['participant'].append(userName)
    target['IDs'].append(userID)

    target_name = target['participant']
    target_id = target['IDs']

    card_collection.update_one({'_id':bson_id},{'$set':{'participant':target_name}})
    card_collection.update_one({'_id':bson_id},{'$set':{'IDs':target_id}})
    card_collection.update_one({'_id':bson_id},{'$set':{'numbers':len(target_name)}})

    print(card_collection.find_one({'_id':bson_id}))
    return jsonify({'result': 'success'})


@bp.route('/main/registration', methods=['POST'])
def posting():
    userID = "TEMPID"
    userName = "TEMPNAME"
    receive_acname = request.form['give_acname']
    receive_acmaxnum = request.form['give_acmaxnum']
    receive_time = request.form['give_time']
    receive_place = request.form['give_place']
    receive_content = request.form['give_content']
    
    participant = [userName]
    IDs = [userID]
    numbers = len(participant)
    print("-" * 20)
    print("dbitems:", receive_acname, receive_acmaxnum, receive_time, receive_place, receive_content, numbers, participant, IDs)
    print("-" * 20)
    doc = {
        'acname' : receive_acname,
        'acmaxnum' : receive_acmaxnum,
        'time' : receive_time,
        'place' : receive_place,
        'content' : receive_content,
        'numbers' : numbers,
        'participant' : participant,
        'IDs' : IDs
        }

    card_collection.insert_one(doc)

    print("doc:",doc)

    return jsonify({'result': 'success'})