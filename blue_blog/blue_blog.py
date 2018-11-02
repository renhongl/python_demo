
from blueblog.blueprints.auth import auth_bp
from blueblog.blueprints.blog import blog_bp

from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/wangyi'
mongo = PyMongo(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(blog_bp, url_prefix='/blog')
