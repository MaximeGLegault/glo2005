from typing import Dict

class Artist:

    def __init__(self):
        self.artist_id = 0
        self.name = ""
        self.year_active = 0

    def to_dict(self) -> Dict:
        return {
            "artist_id": self.artist_id,
            "name": self.name,
            "year_active": self.year_active
        }
