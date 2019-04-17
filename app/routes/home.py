from datetime import date, datetime
from flask import Blueprint, render_template

home = Blueprint('home', __name__, url_prefix='/')


@home.route('/')
def main_route():
    return str(datetime.utcnow())
