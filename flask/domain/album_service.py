from flask import current_app
from typing import Dict, List

from domain.album import Album
from infrastructure.persistence.album_repository_mysql import AlbumRepositoryMysql, AlbumNotFound


class AlbumService:
    def __init__(self):
        self.album_repository = AlbumRepositoryMysql(current_app.config["database_connector"])

    def get_album(self, album_id: int) -> Album:
        return self.album_repository.retrive(album_id)

    def search_album(self, title):
        try:
            album = self.album_repository.search_by_album_title(title)
            print("AlbumNotFound pas raised")
        except AlbumNotFound:
            print("Impossibletogetalbum was raised")
            raise ImpossibleToGetAlbum("Album with title %s does not exist".format(title))
        print("album was returned")
        return album


class ImpossibleToGetAlbum(Exception):

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message

    def to_dict(self) -> Dict:
        return {
            "message": self.message,
        }