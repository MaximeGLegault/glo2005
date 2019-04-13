from flask import Blueprint, request, make_response, jsonify

from domain.user_service import UserService, ConflictSignup
import re


authentication = Blueprint("authentication", __name__, url_prefix="/api")


@authentication.route("/login", methods=['POST'])
def login():
    content = request.get_json()
    username = get_username_if_valid(content["username"])
    password = get_password_if_valid(content["password"])

    token = UserService().login(username, password)

    response = jsonify({"token": token})
    response.headers['location'] = 'users/' + username

    return response


@authentication.route("/signup", methods=["POST"])
def signup():
    content = request.get_json()
    username = get_username_if_valid(content.get("username"))
    email = get_email_if_valid(content.get("email"))
    password = get_password_if_valid(content.get("password"))

    UserService().signup(username, email, password)

    response = make_response("", 201)
    response.headers["location"] = 'users/' + username

    return response


def get_username_if_valid(username: [str, int, float]) -> str:
    if not isinstance(username, (str, int, float)):
        raise InvalidCredentials("username must be a string or a number")

    username = username if isinstance(username, str) else str(username)

    if len(username) < 8:
        raise InvalidCredentials("username must be at least 8 characters")

    if len(username) > 64:
        raise InvalidCredentials("username must be less than 64 characters")

    return username


def get_email_if_valid(email: [str, int, float]) -> str:
    if not isinstance(email, (str, int, float)):
        raise InvalidCredentials("email is invalid")

    email = email if isinstance(email, str) else str(email)

    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    if match == None:
        raise InvalidCredentials("invalid email")

    if len(email) > 64:
        raise InvalidCredentials("email must be less than 64 characters")

    return email


def get_password_if_valid(password: [str, int, float, dict, list]) -> str:
    if not isinstance(password, (str, int, float)):
        raise InvalidCredentials("password must be a string or a number")

    password = password if isinstance(password, str) else str(password)

    if len(password) < 8:
        raise InvalidCredentials("password must be at least 8 characters long")

    if len(password) > 50:
        raise InvalidCredentials("password must be less than 50 characters long")

    return password


def init_authentication_error_handler(app):
    @app.errorhandler(InvalidCredentials)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @app.errorhandler(ConflictSignup)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response


class InvalidCredentials(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
