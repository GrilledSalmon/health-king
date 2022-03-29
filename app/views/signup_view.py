from flask import Blueprint, render_template

bp = Blueprint('user',__name__)

@bp.route('/user')
def user():
    #어쩌고 저쩌고~~
    return render_template('index.html')