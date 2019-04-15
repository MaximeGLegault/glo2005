import flask_bcrypt
from flask import Flask
from flask_cors import CORS

from infrastructure.persistence.database_initialisation import init_bd_mysql
from routes.albums import albums
from routes.authentication import authentication, init_authentication_error_handler
from routes.home import home
from routes.playlists import playlists, init_playlists_error_handler
from routes.profiles import profiles
from routes.songs import songs


def create_app():
    app = Flask(__name__, static_folder="./static", template_folder="./static")
    CORS(app)
    bcrypt = flask_bcrypt.Bcrypt(app)

    # infrastructure initialization and registration
    init_bd_mysql(app)
    app.config["hasher"] = bcrypt

    # error handlers
    init_authentication_error_handler(app)
    init_playlists_error_handler(app)

    # blueprint routes registration
    app.register_blueprint(home)
    app.register_blueprint(authentication)
    app.register_blueprint(albums)
    app.register_blueprint(songs)
    app.register_blueprint(profiles)
    app.register_blueprint(playlists)

    return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0')
