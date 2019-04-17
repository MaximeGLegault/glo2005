from flask import Blueprint, jsonify

from domain.artist_service import ArtistService

artists = Blueprint("artists", __name__, url_prefix="/api")


@artists.route("/artists/<int:artist_id>", methods=['GET'])
def get_artist(artist_id: int):
    album = ArtistService().get(artist_id)
    return jsonify(album.to_dict())


@artists.route("/artists", methods=['GET'])
def get_all_artists():
    artists = ArtistService().get_all_artists()
    return jsonify([artist.to_dict() for artist in artists])
