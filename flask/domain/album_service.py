from flask import current_app

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
        except AlbumNotFound:
            raise ImpossibleToGetAlbum("Album with title %s does not exist".format(title))
        return album


class ImpossibleToGetAlbum(Exception):
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