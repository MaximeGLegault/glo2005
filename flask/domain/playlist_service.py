from flask import current_app

from domain.Playlist import Playlist
from infrastructure.persistence.playlist_repository_mysql import PlaylistRepositoryMysql


class PlaylistService:
    def __init__(self):
        self.playlist_repository = PlaylistRepositoryMysql(current_app.config["database_connector"])

    def get(self, playlist_id: int) -> Playlist:
        playlist = self.playlist_repository.get(playlist_id)

        return playlist
