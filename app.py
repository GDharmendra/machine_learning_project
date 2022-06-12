from re import A
from flask import Flask

app= Flask(__name__)


@app.route("/", methods = ["GET","POST"])
def index():
    return "Starting machine learning project"

if __name__ == "main":
    app.run(debug = True)