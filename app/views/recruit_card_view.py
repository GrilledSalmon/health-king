from flask import Blueprint, render_template

bp = Blueprint('recruit_card',__name__)

@bp.route('/recruit_card')
def recruit_card():
    return render_template('index.html')