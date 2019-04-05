from flask import Blueprint, request, jsonify, url_for, make_response

from domain.user_service import UserService

search = Blueprint("search", __name__, url_prefix="/search")

