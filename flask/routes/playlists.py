from flask import Blueprint, jsonify, make_response, request

from domain.playlist_service import PlaylistService, ImpossibleToGetPlaylist, ImpossibleToDeletePlaylist
from routes.authentication import login_required

playlists = Blueprint("playlists", __name__, url_prefix="/api")


@playlists.route('/playlists/<int:playlist_id>', methods=["GET"])
def get_profile(playlist_id):
    playlist = PlaylistService().get(playlist_id)

    return jsonify(playlist.to_dict())

@playlists.route('/playlists', methods=["GET"])
@login_required
def get_user_playlists(**kwargs):
    user_id = kwargs["user_id"]
    playlist = PlaylistService().get_user_playlists(user_id)

    ret_playlists =[]
    for play in playlist:
        ret_playlists.append(play.to_dict())

    return jsonify(ret_playlists)


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


@playlists.route('/playlists/<playlist_id>', methods=["POST"])
@login_required
def add_song_to_playlist(playlist_id, **kwargs):
    content = request.get_json()
    song_id = content["song_id"]
    playlist_id = PlaylistService().add_song(playlist_id, song_id)

    return make_response(jsonify({'playlist_id': playlist_id}), 201)

@playlists.route('/playlists/liked', methods=["POST"])
@login_required
def like_song(**kwargs):
    user_id = kwargs["user_id"]
    content = request.get_json()
    song_id = content["song_id"]
    song_id = PlaylistService().like_song(user_id,song_id)

    return make_response(jsonify({'song_id': song_id}), 201)

@playlists.route('/playlists/liked', methods=["DELETE"])
@login_required
def unlike_song(**kwargs):
    user_id = kwargs["user_id"]
    content = request.get_json()
    song_id = content["song_id"]
    song_id = PlaylistService().unlike_song(user_id, song_id)

    return make_response(jsonify({'song_id': song_id}), 201)

def init_playlists_error_handler(app):
    @app.errorhandler(ImpossibleToGetPlaylist)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @app.errorhandler(ImpossibleToDeletePlaylist)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response
