from functools import wraps

from flask import Blueprint, request, make_response, jsonify
from werkzeug.exceptions import BadRequest

from domain.user_service import UserService, ConflictSignup, CannotLogin
import re

from infrastructure.jwt_service import JWTService, InvalidToken

authentication = Blueprint("authentication", __name__, url_prefix="/api")


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            token: str = request.headers.get("Authorization")
        except BadRequest:
            response = jsonify({"message": "couldn't parse your json"})
            response.status_code = 401
            return response

        if token is None or not token.startswith("Bearer "):
            response = jsonify({"message": "you need to pass a valid bearer token!"})
            response.status_code = 401
            return response

        _, _, token = token.partition("Bearer ")

        try:
            username, user_id = JWTService().decode_token(token)
        except InvalidToken:
            response = jsonify({"message": "you need to pass a token!"})
            response.status_code = 401
            return response

        kwargs['username'] = username
        kwargs["user_id"] = user_id

        return f(*args, **kwargs)
    return decorated_function


@authentication.route("/login", methods=['POST'])
def login():
    content = request.get_json()
    username = get_username_if_valid(content["username"])
    password = get_password_if_valid(content["password"])

    token = UserService().login(username, password)

    response = jsonify({"token": token, "username": username})
    response.headers['location'] = 'users/' + username

    return response


@authentication.route("/signup", methods=["POST"])
def signup():
    content = request.get_json()
    username = get_username_if_valid(content.get("username"))
    email = get_email_if_valid(content.get("email"))
    password = get_password_if_valid(content.get("password"))

    token = UserService().signup(username, email, password)

    response = make_response(jsonify({"token": token, "username": username}), 201)
    response.headers["location"] = 'users/' + username

    return response


@authentication.route("/token", methods=['GET'])
@login_required
def get_token_info(**kwargs):
    username = kwargs['username']

    return jsonify({"message": "this token is valid", "username": username})


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

    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
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

    @app.errorhandler(CannotLogin)
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
