from typing import Dict


class Album:
    def __init__(self):
        self.id = 0
        self.year = 0
        self.genre = ""
        self.title = ""
        self.description = ""
        self.artist_name = ""

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "year": self.year,
            "genre": self.genre,
            "title": self.title,
            "description": self.description,
            "artistName": self.artist_name,
        }
