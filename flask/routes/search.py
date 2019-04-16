from flask import Blueprint, request, jsonify, url_for, make_response

from domain.album_service import AlbumService, ImpossibleToGetAlbum
from domain.artist_service import ArtistService, ImpossibleToGetArtist
from domain.song_service import SongService, ImpossibleToGetSong

search = Blueprint("search", __name__, url_prefix="/api")


@search.route("/search/albums/<title>", methods=['GET'])
def search_album(title):
    albums_list = AlbumService().search_album(title)
    return jsonify([album.to_dict() for album in albums_list])

@search.route("/search/artists/<artist_name>", methods=['GET'])
def search_artist(artist_name):
    artists_list = ArtistService().search_artist(artist_name)
    return jsonify([artist.to_dict() for artist in artists_list])

@search.route("/search/songs/<title>", methods=['GET'])
def search_song(title):
    songs_list = SongService().search_song(title)
    return jsonify([song.to_dict() for song in songs_list])

@search.route("/search/artists/<int:artist_id>", methods=['GET'])
def search_artist_by_id(artist_id):
    artist = ArtistService().get_Artist(artist_id)
    return jsonify(artist.to_dict())


def init_search_error_handler(app):
    @app.errorhandler(ImpossibleToGetAlbum)
    def handle_inexistent_album(error):
        print(error)
        response = jsonify(error.to_dict())
        return response

    @app.errorhandler(ImpossibleToGetArtist)
    def handle_inexistent_artist(error):
        print(error)
        response = jsonify(error.to_dict())
        return response

    @app.errorhandler(ImpossibleToGetSong)
    def handle_inexistent_song(error):
        print(error)
        response = jsonify(error.to_dict())
        return response
