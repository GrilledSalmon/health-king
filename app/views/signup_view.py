from flask import Blueprint, render_template, request, jsonify
from app import user_collection
bp = Blueprint('signup_view',__name__)

@bp.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == "POST":
        # 유저 저장
        # req = request.form
        # id = req['id']
        # password = req['password']
        # name = req['name']
        print(request.form)
        print(type(request.form))
        # user_collection.insert_one(request.form)
        user_collection.insert_one
        
        return jsonify({'result' : 'success'})
    else:
        return render_template('signup.html')
    

    

@bp.route('/user/check', methods=['POST'])
def user_check():
    # 유저 아이디 중복체크

    return render_template('index.html')
