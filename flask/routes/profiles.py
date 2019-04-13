from flask import Blueprint, jsonify

from domain.profile_service import ProfileService
from routes.authentication import login_required

profiles = Blueprint("profiles", __name__, url_prefix="/api")


@profiles.route('/profiles', methods=["GET"])
@login_required
def get_profile(username: str):
    playlists = ProfileService().get_profile(username)

    return jsonify([playlist.to_dict() for playlist in playlists])
