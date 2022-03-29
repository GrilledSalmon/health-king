from flask import Blueprint, render_template, request, jsonify
from app import user_collection
bp = Blueprint('signup_view',__name__)

@bp.route('/user', methods=['GET', 'POST'])
def user():
    """회원가입한 유저 데이터 저장 및 회원가입 페이지 보여주기"""
    if request.method == "POST":
        # 유저 데이터 저장
        # doc 형태 : {'id' : id, 'password' : password, 'name' : name}
        user_collection.insert_one(dict(request.form))
        
        return jsonify({'result' : 'success'})
    
    # GET인 경우    
    return render_template('signup.html')
    

@bp.route('/user/check', methods=['POST'])
def user_id_check():
    # 유저 아이디 중복체크
    new_id = request.form['id']
    if user_collection.find_one({'id':new_id}):
        return jsonify({'result' : 'fail'})

    return jsonify({'result' : 'success'})
