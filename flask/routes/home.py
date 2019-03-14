from flask import Blueprint, render_template

home = Blueprint('home', __name__, url_prefix='/')


@home.route('/', defaults={'path': ''})
@home.route('/<path:path>')
def main_route(path):
    return render_template("index.html")
