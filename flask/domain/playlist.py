from typing import Dict


class Playlist:

    def __init__(self):
        self.title = ""
        self.songs = []
        self.user_id = 0
        self.playlist_id = 0

    def to_dict(self) -> Dict:
        dict_to_return = {
            "title": self.title,
            "user_id": self.user_id,
            "playlist_id": self.playlist_id
        }

        if self.songs:
            dict_to_return["songs"] = [song.to_dict() for song in self.songs]

        return dict_to_return
