from typing import List

from flask import current_app

from domain.song import Song
from infrastructure.persistence.song_repository_mysql import SongRepositoryMysql


class SongService:
    def __init__(self):
        self.song_repository = SongRepositoryMysql(current_app.config["database_connector"])

    def get_song(self, song_id: int) -> Song:
        return self.song_repository.retrieve(song_id)

    def get_all_song_from_album(self, album_id: int) -> List[Song]:
        return self.song_repository.retrieve_all_from_album(album_id)


