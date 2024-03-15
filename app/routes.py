from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Sarma"}
    posts = [
        {"author": {"username": "Sarma"}, "body": "Beautiful day in Sydney!"},
        {"author": {"username": "Sami"}, "body": "The Avengers movie was so cool!"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
