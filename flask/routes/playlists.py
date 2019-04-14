from flask import Blueprint, jsonify, make_response, request

from domain.playlist_service import PlaylistService
from routes.authentication import login_required

playlists = Blueprint("playlists", __name__, url_prefix="/api")


@playlists.route('/playlists/<int:playlist_id>', methods=["GET"])
def get_profile(playlist_id):
    playlist = PlaylistService().get(playlist_id)

    return jsonify(playlist.to_dict())


@playlists.route('/playlists/<int:playlist_id>', methods=["DELETE"])
@login_required
def delete_playlist(playlist_id: int, **kwargs):
    user_id = kwargs["user_id"]
    PlaylistService().delete(user_id, playlist_id)

    return make_response("", 204)


@playlists.route('/playlists', methods=["POST"])
@login_required
def create_playlist(**kwargs):
    user_id = kwargs["user_id"]
    title = request.get_json()["title"]
    playlist_id = PlaylistService().add(user_id, title)

    return make_response(jsonify({'playlist_id': playlist_id}), 201)
