from typing import List

from mysql.connector import MySQLConnection

from domain.Playlist import Playlist


class PlaylistRepositoryMysql:
    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def get_playlist_from_username(self, username: str) -> List[Playlist]:
        cursor = self.database_connector.cursor()
        query = "SELECT id FROM Users WHERE username = %s"

        cursor.execute(query, (username,))
        user_id,  = cursor.fetchone()

        query = "SELECT playlist_id, title FROM Playlists WHERE playlist_id = " \
                "(SELECT playlist_id FROM Users_Playlists WHERE user_id = %s)"
        cursor.execute(query, (user_id,))

        playlists = []
        for playlist_id, title in cursor:
            playlist = Playlist()
            playlist.user_username = username
            playlist.user_id = user_id
            playlist.playlist_id = playlist_id
            playlist.title = title

            playlists.append(playlist)

        cursor.close()
        return playlists
