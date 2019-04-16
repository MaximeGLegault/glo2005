from flask import Blueprint, jsonify

from domain.artist_service import ArtistService

artists = Blueprint("artists", __name__, url_prefix="/api")


@artists.route("/artists/<int:artist_id>", methods=['GET'])
def get_album(artist_id: int):
    album = ArtistService().get(artist_id)
    return jsonify(album.to_dict())
