from flask import Blueprint, jsonify

from domain.song_service import SongService

songs = Blueprint("songs", __name__, url_prefix="/api")


@songs.route("/albums/<int:album_id>/songs/<int:song_id>", methods=['GET'])
def get_particular_song_from_album(album_id: int, song_id: int):
    song = SongService().get_song(song_id)

    return jsonify(song.to_dict())


@songs.route("/albums/<int:album_id>/songs", methods=['GET'])
def get_all_songs_from_album(album_id: int):
    songs_from_album = SongService().get_all_song_from_album(album_id)

    return jsonify([song.to_dict() for song in songs_from_album])


@songs.route("/songs", methods=['GET'])
def get_all_songs():
    songs = SongService().get_all_songs()
    return jsonify([song.to_dict() for song in songs])
