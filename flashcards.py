from flask import Flask, render_template,abort
from model import load_db
# from datetime import datetime

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my Flash Cards application."

@app.route('/card/<int:index>')
def card_view(index):
    # return "Welcome to my Flash Cards application."
    try:
        db = load_db()
        card = db[index]
        return render_template("cards.html",message = "Hey I just used a jinga variable for the first time.",card=card)
    except:
        abort(404)
"""
@app.route('/date')
def date():
    return "The page was served at " +str(datetime.now())

counter = 0

@app.route('/count_views')
def count_views():
    global counter
    counter+=1
    return "This page was served "+ str(counter) + " times"
"""