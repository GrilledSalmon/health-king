from flask import Flask, render_template
from pymongo import MongoClient
from .views import login_view, signup_view, recruit_card_view
from .secrets import HOST, PORT, USERNAME, PASSWORD

client = MongoClient(
    HOST,
    PORT,
    username=USERNAME,
    password=PASSWORD
)
db = client['health']

user_collection = db.user
card_collection = db.card


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# devsds
app.register_blueprint(login_view.bp)
app.register_blueprint(signup_view.bp)
app.register_blueprint(recruit_card_view.bp)
