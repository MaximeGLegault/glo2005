from flask import Blueprint, jsonify

from domain.playlist_service import PlaylistService

playlists = Blueprint("playlists", __name__, url_prefix="/api")


@playlists.route('/playlists/<int:playlist_id>', methods=["GET"])
def get_profile(playlist_id):
    playlist = PlaylistService().get(playlist_id)

    return jsonify(playlist.to_dict())
