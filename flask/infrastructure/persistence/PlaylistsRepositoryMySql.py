from mysql.connector import MySQLConnection

from domain.playlist import Playlist


class PlaylistsRepositoryMySql:

    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def search_by_playlist(self, title: str) -> str:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Playlists WHERE title LIKE %s"
        cursor.execute(query, (title,))

        playlist_title = None
        for (id, title) in cursor:
            playlist_title = title

        cursor.close()
        return playlist_title
