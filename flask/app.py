import flask_bcrypt
from flask import Flask
from flask_cors import CORS

from infrastructure.persistence.database_initialisation import init_bd_mysql
from routes.authentication import authentication, init_authentication_errorhandler
from routes.home import home


def create_app():
    app = Flask(__name__, static_folder="./static", template_folder="./static")
    CORS(app)
    bcrypt = flask_bcrypt.Bcrypt(app)

    # infrastructure initialization and registration
    init_bd_mysql(app)
    app.config["hasher"] = bcrypt

    # error handlers
    init_authentication_errorhandler(app)

    # blueprint routes registration
    app.register_blueprint(home)
    app.register_blueprint(authentication)

    return app

if __name__ == '__main__':
    create_app().run()
