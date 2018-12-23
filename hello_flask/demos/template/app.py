
from flask import Flask, render_template
import os

user = {
    'username': 'renhongl'
}

movies = [
    {
        'name': '琅琊榜',
        'year': '2017'
    },
    {
        'name': '西游记',
        'year': '1986'
    }
]

path = os.path.abspath('./demos/template/templates')
static = os.path.abspath('./demos/template/static')
app = Flask(__name__, template_folder=path, static_folder=static)

@app.route('/')
def index():
    return 'Index'

@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)

@app.errorhandler(404)
def page_not_found(e):
    return '404'