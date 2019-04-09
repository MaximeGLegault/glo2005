from mysql.connector import MySQLConnection

from domain.song import Song


class SongsRepositoryMySql:

    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def search_by_song(self, title: str) -> Song.title:
        cursor = self.database_connector.cursor()
        print(title)
        query = "SELECT * FROM Songs WHERE title LIKE %s"
        cursor.execute(query, (title,))

        title = None
        for (id, title, artist, album, duration) in cursor:
            title = Song(title, artist, album, duration)

        cursor.close()
        return title


