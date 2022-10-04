from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def connect_to_wordbot():
    return render_template ('base_home.html')