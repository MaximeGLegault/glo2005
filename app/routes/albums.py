from flask import Blueprint, jsonify

from domain.album_service import AlbumService

albums = Blueprint("albums", __name__, url_prefix="/api")


@albums.route("/albums/<int:album_id>", methods=['GET'])
def get_album(album_id: int):
    album = AlbumService().get_album(album_id)
    return jsonify(album.to_dict())


@albums.route("/albums", methods=['GET'])
def get_all_albums():
    albums = AlbumService().get_all_albums()
    return jsonify([album.to_dict() for album in albums])

