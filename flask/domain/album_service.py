from flask import current_app

from domain.album import Album
from infrastructure.persistence.album_repository_mysql import AlbumRepositoryMysql


class AlbumService():
    def __init__(self):
        self.album_repository = AlbumRepositoryMysql(current_app.config["database_connector"])

    def get_album(self, album_id: int) -> Album:
        return self.album_repository.retrive(album_id)
