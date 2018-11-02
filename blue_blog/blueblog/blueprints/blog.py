
from flask import Blueprint

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/about')
def about():
    return 'about'

@blog_bp.route('/category/<int:category_id>')
def category(category_id):
    return 'category_id'