
from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        name = request.args.get('name')
        return '<h1>%s</h1>' % name
    elif request.method == 'POST':
        data = request.json
        return '<h1>%s</h1>' % data['name']

@app.route('/student')
def student():
    stu = {
        'name': 'renhongl',
        'age': 18,
        'gender': 'male'
    }
    return jsonify(stu)

@app.route('/teacher')
def teacher():
    tea = {
        'name': 'laoshi',
        'age': '45'
    }
    response = make_response(json.dumps(tea))
    response.mimetype = 'application/json'
    return response