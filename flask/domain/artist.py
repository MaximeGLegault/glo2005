from typing import Dict


class Artist:

    def __init__(self):
        self.artist_id = 0
        self.artist_name = ""
        self.year_active = 0
        self.albums = []

    def to_dict(self) -> Dict:
        dict_to_return = {
            "artist_id": self.artist_id,
            "artist_name": self.artist_name,
            "year_active": self.year_active
        }

        if self.albums:
            dict_to_return["albums"] = [album.to_dict() for album in self.albums]

        return dict_to_return
