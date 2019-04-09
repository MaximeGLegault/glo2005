from typing import Dict


class Song:
    def __init__(self):
        self.id = 0
        self.artist_name = ""
        self.year = 0
        self.genre = ""
        self.title = ""
        self.duration = 0
        self.albumId = 0

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "artistName": self.artist_name,
            "year": self.year,
            "genre": self.genre,
            "title": self.title,
            "duration": self.duration,
            "albumId": self.albumId
        }
