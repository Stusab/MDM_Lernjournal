from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello from MDM Woche 1 </h1>"
