from flask import Blueprint, request, jsonify

authentication = Blueprint("authentication", __name__, url_prefix="/api")


@authentication.route("/login", methods=['POST'])
def login():
    content = request.get_json()
    print(content)
    return jsonify({"token": "token"})


@authentication.route("/signup", methods=["POST"])
def signup():
    content = request.get_json()
    print(content)
    return jsonify({"token": "token"})

