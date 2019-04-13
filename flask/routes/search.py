from flask import Blueprint, request, jsonify, url_for, make_response

from domain.album_service import AlbumService
from domain.artist_service import ArtistService

search = Blueprint("search", __name__, url_prefix="/api")


@search.route("/search/albums/<str:title>", methods=['GET'])
def search_album(title: str):
    print("search_album called")
    album = AlbumService().search_album(title)
    return jsonify(album.to_dict())
