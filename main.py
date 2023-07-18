from flask import Flask, url_for    
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login/')
def login():
    return 'login lmao'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'