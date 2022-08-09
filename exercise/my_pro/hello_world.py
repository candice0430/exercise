from flask import Flask, url_for,render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html',)

with app.test_request_context():
    print(url_for('hello'))
    print("123")