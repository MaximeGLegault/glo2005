from flask import current_app

from domain.playlist import Playlist
from infrastructure.persistence.playlist_repository_mysql import PlaylistRepositoryMysql, PlaylistNotFound


class PlaylistService:
    def __init__(self):
        self.playlist_repository = PlaylistRepositoryMysql(current_app.config["database_connector"])

    def get(self, playlist_id: int) -> Playlist:
        try:
            playlist = self.playlist_repository.get(playlist_id)
        except PlaylistNotFound:
            raise ImpossibleToGetPlaylist("Playlist with id %s does not exist".format(playlist_id))

        return playlist

    def get_user_playlists(self,user_id):
        return self.playlist_repository.get_playlist_from_username(user_id)

    def like_song(self,user_id, song_id):
        return self.playlist_repository.like_song(user_id,song_id)

    def unlike_song(self,user_id, song_id):
        return self.playlist_repository.unlike_song(user_id,song_id)

    def delete(self, user_id: str,  playlist_id: int) -> None:
        if self.playlist_repository.is_playlist_by_user(user_id, playlist_id):
            self.playlist_repository.delete(playlist_id)
            return

        raise ImpossibleToDeletePlaylist("Couldn't delete the playlist, either it doesn't exist"
                                         "or it is not one of this user's playlist.")

    def add(self, user_id: int, title: str) -> int:
        return self.playlist_repository.add_playlist_to_user(user_id, title)

    def add_song(self, playlist_name, song_id):
        return self.playlist_repository.add_song_to_playlist(playlist_name, song_id)

class ImpossibleToGetPlaylist(Exception):
    status_code = 404

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class ImpossibleToDeletePlaylist(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
