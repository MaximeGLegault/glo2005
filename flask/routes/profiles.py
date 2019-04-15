from flask import Blueprint, jsonify

from domain.profile_service import ProfileService
from routes.authentication import login_required

profiles = Blueprint("profiles", __name__, url_prefix="/api")


# is of no use right now!
@profiles.route('/profiles', methods=["GET"])
@login_required
def get_profile(**kwargs):
    user_id = kwargs["user_id"]

    playlists = ProfileService().get_profile(user_id)

    return jsonify([playlist.to_dict() for playlist in playlists])


@profiles.route('/profile', methods=["GET"])
@login_required
def get_own_profile(**kwargs):
    user_id = kwargs["user_id"]

    playlists = ProfileService().get_profile(user_id)

    return jsonify([playlist.to_dict() for playlist in playlists])
