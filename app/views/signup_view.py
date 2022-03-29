from flask import Blueprint, render_template

bp = Blueprint('user',__name__)

@bp.route('/user')
def user():
    return render_template('index.html')