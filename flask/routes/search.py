from flask import Blueprint, request, jsonify, url_for, make_response

from domain.album_service import AlbumService
from domain.artist_service import ArtistService

search = Blueprint("search", __name__, url_prefix="/api")


@search.route("/search/albums/<title>", methods=['GET'])
def search_album(title):
    print("search_album called")
    album = AlbumService().search_album(title)
    return jsonify(album.to_dict())


@search.route("/search/artists/<name>", methods=['GET'])
def search_artist(name):
    print("search_artist called")
    artist = ArtistService().search_artist(name)
    return jsonify(artist.to_dict())


@search.route("/search/artists/<int:artist_id>", methods=['GET'])
def search_artist_by_id(artist_id):
    print("search_artist_by_id called")
    artist = ArtistService().get_Artist(artist_id)
    return jsonify(artist.to_dict())



