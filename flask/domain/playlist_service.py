from flask import current_app

from domain.Playlist import Playlist
from infrastructure.persistence.playlist_repository_mysql import PlaylistRepositoryMysql


class PlaylistService:
    def __init__(self):
        self.playlist_repository = PlaylistRepositoryMysql(current_app.config["database_connector"])

    def get(self, playlist_id: int) -> Playlist:
        playlist = self.playlist_repository.get(playlist_id)

        return playlist

    def delete(self, user_id: str,  playlist_id: int) -> None:
        if self.playlist_repository.is_playlist_by_user(user_id, playlist_id):
            self.playlist_repository.delete(playlist_id)
            return

        raise Exception("sdf")

    def add(self, user_id: int, title: str) -> int:
        return self.playlist_repository.add_playlist_to_user(user_id, title)
