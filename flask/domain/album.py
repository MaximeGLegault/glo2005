from typing import Dict


class Album:
    def __init__(self):
        self.album_id = 0
        self.title = ""
        self.year = 0
        self.genre_id = 0
        self.genre_name = ""
        self.artist_id = 0
        self.artist_name = ""
        self.songs = []

    def to_dict(self) -> Dict:
        return {
            "album_id": self.album_id,
            "title": self.title,
            "year": self.year,
            "genre_id": self.genre_id,
            "genre": self.genre_name,
            "artist_id": self.artist_id,
            "artist_name": self.artist_name,
            "songs": [song.to_dict() for song in self.songs]
        }