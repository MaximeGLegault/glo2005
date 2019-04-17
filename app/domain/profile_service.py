from typing import List

from flask import current_app

from domain.playlist import Playlist
from infrastructure.jwt_service import JWTService
from infrastructure.persistence.playlist_repository_mysql import PlaylistRepositoryMysql


class ProfileService():
    def __init__(self):
        self.jwt_service = JWTService()
        self.playlist_repository = PlaylistRepositoryMysql(current_app.config["database_connector"])

    def get_profile(self, user_id: int) -> List[Playlist]:
        return self.playlist_repository.get_playlist_from_username(user_id)
