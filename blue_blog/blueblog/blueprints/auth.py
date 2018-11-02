
from flask import Blueprint
from blue_blog import mongo

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login')
def login():
    items = mongo.db['可乐'].find()
    return items


@auth_bp.route('/logout')
def logout():
    return 'logout'