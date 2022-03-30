from flask import Blueprint, render_template, request,abort, make_response, jsonify
from app.secrets import SECRET_KEY
from app import user_collection
from bcrypt import checkpw
from bson.objectid import ObjectId
import datetime
import jwt

def encode_token(object_id):
        payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, minutes=30),
                'iat': datetime.datetime.utcnow(),
                'sub': 'health_king_token',
                'object_id':object_id
            }
        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )


bp = Blueprint('login',__name__)

@bp.route('/login', methods=["POST"])
def login():
    if request.method != "POST":
        abort(404)

    # 원래 코드, form요청임
    # user_id = request.form.get('user-id')
    # user_pw = str(request.form.get('user-pw'))

    # 임시 코드, json요청
    data = request.get_json()
    # print(data)
    
    # 키: user-id, user-pw
    user_id = data['user-id']
    user_pw = data['user-pw']
    
    # id check
    user = user_collection.find_one({'id':user_id})
    # 일치하는 id가 없으면 404 not found
    if not user:
        return "no user", 404

    # pw check
    # db의 password와 일치하지 않으면 403 Forbidden
    if not checkpw(password=user_pw.encode(), hashed_password=user['password']):
        return "비밀번호가 틀렸습니다", 403


    ##### 세션 방식 #####
    # # 로그인 성공시 세션에 id와 이름을 저장
    # session['id'] = user['id']
    # session['name'] = user['name']
    # print("로그인 성공")
    # return render_template('index.html')
    # print(user.keys())
    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'access_token': encode_token(str(user['_id'])),
                    }


    return make_response(jsonify(responseObject)), 200


# @bp.route('/logout', methods=['GET'])
# def logout():
#     session.clear()
#     return redirect(url_for('home'))