from flask import Flask, render_template
from flask_cors import CORS
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
    CORS(app)
    app.secret_key = SECRET_KEY

    @app.route('/', methods=['GET'])
    def home():
        return render_template('index.html')

    from .views import login_view, signup_view, recruit_card_view
    app.register_blueprint(login_view.bp)
    app.register_blueprint(signup_view.bp)
    app.register_blueprint(recruit_card_view.bp)

    return app

@app.route('/main', methods=['GET'])
def listing():

    result = list(db.health.find({}))

    for i in range(len(result)):
        temp_id = str(result[i]['_id']) 
        del result[i]['_id'] 
        result[i]['_id'] = temp_id 

    return jsonify({'result':'success', 'activities': result})



@app.route('/main/registration', methods=['POST'])
def posting():
    receive_acname = request.form['give_acname']
    receive_time = request.form['give_time']
    receive_place = request.form['give_place']
    receive_content = request.form['give_content']

    print("sadfefe",receive_acname, receive_time, receive_place, receive_content)

    doc = {
        'acname' : receive_acname,
        'time' : receive_time,
        'place' : receive_place,
        'content' : receive_content
        }

    db.health.insert_one(doc)

    print("doc:",doc)

    return jsonify({'result': 'success'})

# devsds
app.register_blueprint(login_view.bp)
app.register_blueprint(signup_view.bp)
app.register_blueprint(recruit_card_view.bp)
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
