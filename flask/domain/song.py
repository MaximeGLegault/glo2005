from typing import Dict


class Song:
    def __init__(self):
        self.song_id = 0
        self.artist_name = ""
        self.genre = ""
        self.title = ""
        self.duration = 0
        self.album_id = 0
        self.album_name = ""

    def to_dict(self) -> Dict:
        return {
            "song_id": self.song_id,
            "artistName": self.artist_name,
            "genre": self.genre,
            "title": self.title,
            "duration": self.duration,
            "albumId": self.album_id,
            "album_name": self.album_name
        }
