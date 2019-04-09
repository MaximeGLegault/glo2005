from mysql.connector import MySQLConnection

from domain.album import Album


class AlbumsRepositoryMySql:

    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def search_by_album(self, album: str) -> Album.title:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Albums WHERE title LIKE %s"
        cursor.execute(query, (album,))

        album = None
        for (id, title, artist, genre, released) in cursor:
            album = Album(title, artist, genre, released)

        cursor.close()
        return album