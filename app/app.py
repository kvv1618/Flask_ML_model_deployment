from flask import Flask

app = Flask(__name__)

@app.route("/")
def connect_to_wordbot():
    return {"message":"hi!"}