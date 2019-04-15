from flask import current_app
from typing import Dict

from domain.album import Album
from infrastructure.persistence.album_repository_mysql import AlbumRepositoryMysql, AlbumNotFound


class AlbumService:
    def __init__(self):
        self.album_repository = AlbumRepositoryMysql(current_app.config["database_connector"])

    def get_album(self, album_id: int) -> Album:
        return self.album_repository.retrive(album_id)

    def search_album(self, title: str) -> Album:
        try:
            album = self.album_repository.search_by_album_title(title)
            print("search_album dans album_service was called")
        except AlbumNotFound:
            print("impossibletoGetAlbum was raised")
            raise ImpossibleToGetAlbum("Album with title %s does not exist".format(title))
        return album


class ImpossibleToGetAlbum(Exception):

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message

    def to_dict(self) -> Dict:
        return {
            "message": self.message,
        }