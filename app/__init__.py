from app.views.recruit_card_view import recruit_card
from flask import Flask, render_template
from .views import login_view, signup_view, recruit_card_view



app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# devsds
app.register_blueprint(login_view.bp)
app.register_blueprint(signup_view.bp)
app.register_blueprint(recruit_card_view.bp)
