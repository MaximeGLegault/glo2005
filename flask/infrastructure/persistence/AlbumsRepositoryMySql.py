from mysql.connector import MySQLConnection

from domain.album import Album


class AlbumsRepositoryMySql:

    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def search_by_album(self, title: str) -> Album.title:
        cursor = self.database_connector.cursor()
        print(title)
        query = "SELECT * FROM Albums WHERE title LIKE %s"
        cursor.execute(query, (title,))

        title = None
        for (id, title, artist, songs, genre, duration, released) in cursor:
            title = Album(title, artist, songs, genre, duration, released)

        cursor.close()
        return title
