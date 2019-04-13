

class Playlist:
    def __init__(self):
        self.playlist_id = 0
        self.user_id = 0
        self.user_username = ""
        self.title = ""

    def to_dict(self):
        return {
            "playlist_id": self.playlist_id,
            "user_id": self.user_id,
            "user_username": self.user_username,
            "title": self.title
        }
