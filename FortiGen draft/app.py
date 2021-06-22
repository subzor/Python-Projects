from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def FortiGen():
    return render_template('index.html')

