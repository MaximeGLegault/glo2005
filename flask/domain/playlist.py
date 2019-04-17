from typing import Dict


class Playlist:
    def __init__(self):
        self.playlist_id = 0
        self.user_id = 0
        self.user_username = ""
        self.title = ""
        self.songs = []

    def to_dict(self) -> Dict:
        dict_to_return = {
            "playlist_id": self.playlist_id,
            "user_id": self.user_id,
            "title": self.title
        }

        if len(self.songs) > 0:
            dict_to_return["songs"] = [song.to_dict() for song in self.songs]

        if len(self.user_username) > 0:
            dict_to_return["user_username"] = self.user_username

