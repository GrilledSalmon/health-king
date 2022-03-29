from flask import Flask, render_template
from pymongo import MongoClient
from app.secrets import HOST, PORT, USERNAME, PASSWORD, SECRET_KEY

client = MongoClient(
    HOST,
    PORT,
    username=USERNAME,
    password=PASSWORD
)
db = client['health']

user_collection = db.user
card_collection = db.card


def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY

    @app.route('/', methods=['GET'])
    def home():
        return render_template('index.html')

    from .views import login_view, signup_view, recruit_card_view
    app.register_blueprint(login_view.bp)
    app.register_blueprint(signup_view.bp)
    app.register_blueprint(recruit_card_view.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
