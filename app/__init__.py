from flask import Flask, render_template
from views import login_view



app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


app.register_blueprint(login_view.bp)

# @app.route('/mypage', methods=['GET'])
# def asd():
#     return render_template('mypage.html')

