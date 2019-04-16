from typing import List, Dict

from flask import current_app

from domain.song import Song
from infrastructure.persistence.song_repository_mysql import SongRepositoryMysql, SongNotFound


class SongService:
    def __init__(self):
        self.song_repository = SongRepositoryMysql(current_app.config["database_connector"])

    def get_song(self, song_id: int) -> Song:
        return self.song_repository.retrieve(song_id)

    def get_all_song_from_album(self, album_id: int) -> List[Song]:
        return self.song_repository.retrieve_all_from_album(album_id)

    def search_song(self, title):
        try:
            songs = self.song_repository.search_by_title(title)
        except SongNotFound:
            raise ImpossibleToGetSong("Song with title %s does not exist".format(title))
        return songs

class ImpossibleToGetSong(Exception):

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message

    def to_dict(self) -> Dict:
        return {
            "message": self.message,
        }


