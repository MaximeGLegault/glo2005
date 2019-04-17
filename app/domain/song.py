from typing import Dict


class Song:
    def __init__(self):
        self.song_id = 0
        self.artist_name = ""
        self.artist_id = 0
        self.genre_name = ""
        self.genre_id = 0
        self.title = ""
        self.duration = 0
        self.album_id = 0
        self.album_name = ""

    def to_dict(self) -> Dict:
        return {
            "song_id": self.song_id,
            "artist_name": self.artist_name,
            "artist_id": self.artist_id,
            "genre_name": self.genre_name,
            "genre_id": self.genre_id,
            "title": self.title,
            "duration": self.duration,
            "album_id": self.album_id,
            "album_name": self.album_name
        }
