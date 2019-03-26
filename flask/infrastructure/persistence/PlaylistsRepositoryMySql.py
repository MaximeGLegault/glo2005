from mysql.connector import MySQLConnection

from domain.playlist import Playlist


class PlaylistsRepositoryMySql:

    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def search_by_playlist(self, title: str) -> Playlist.title:
        cursor = self.database_connector.cursor()
        print(title)
        query = "SELECT * FROM Playlists WHERE title LIKE %s"
        cursor.execute(query, (title,))

        title = None
        for (id, title, songs, genre, duration) in cursor:
            title = Playlist(title, songs, genre, duration)

        cursor.close()
        return title
