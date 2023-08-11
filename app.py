from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("pages/home.html")

@app.route("/about")
def about():
    return render_template("pages/about.html")

@app.route("/careers")
def careers():
    return render_template("pages/careers.html")

@app.route("/events")
def events():
    return render_template("pages/events.html")

@app.route("/the-trial")
def the_trial():
    return render_template("pages/the-trial.html")

application = app