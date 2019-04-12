from typing import Dict


class Album:
    def __init__(self):
        self.album_id = 0
        self.year = 0
        self.genre_id = 0
        self.title = ""
        self.artist_id = 0

    def to_dict(self) -> Dict:
        return {
            "album_id": self.album_id,
            "year": self.year,
            "genre_id": self.genre_id,
            "title": self.title,
            "artist_id": self.artist_id,
        }
