
from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask Index</h1>'

@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello Flask</h1>'

@app.route('/greet', defaults={'name': 'default name'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello %s</h1>' % name

@app.route('/redirect')
def go_to_index():
    return redirect(url_for('index'))