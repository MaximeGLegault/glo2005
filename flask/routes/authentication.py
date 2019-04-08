from flask import Blueprint, request, url_for, make_response

from domain.user_service import UserService

authentication = Blueprint("authentication", __name__, url_prefix="/api")


@authentication.route("/login", methods=['POST'])
def login():
    content = request.get_json()
    username = UserService().login(content["username"], content["password"])
    response = make_response(url_for("user", username=username))
    response.headers['location'] = username
    return response


@authentication.route("/signup", methods=["POST"])
def signup():
    content = request.get_json()
    UserService().signup(content["username"], content["password"])
    return url_for("/login")
