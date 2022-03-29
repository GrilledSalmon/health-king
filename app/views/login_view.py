from flask import Blueprint, render_template, request,abort,session
from app import user_collection
bp = Blueprint('login',__name__)

@bp.route('/login', methods=["POST"])
def login():
    if request.method != "POST":
        abort(404)
        return "포스트요청"

    user_id = request.form.get('user-id')
    user_pw = request.form.get('user-pw')
    
    # id check
    user = user_collection.find_one({'id':user_id})
    # 일치하는 id가 없으면 404 not found
    if not user:
        return "no user", 404

    # pw check
    # db의 password와 일치하지 않으면 403 Forbidden
    if user['user_pw'] != user_pw:
        return "비밀번호가 틀렸습니다", 403

    # 로그인 성공시 세션에 id와 이름을 저장
    session['id'] = user['_id']
    session['name'] = user['name']
    
    return render_template('index.html')