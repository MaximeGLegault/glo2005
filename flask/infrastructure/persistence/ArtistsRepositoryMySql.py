from mysql.connector import MySQLConnection

from domain.artist import Artist


class ArtistsRepositoryMySql:

    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def search_by_artist(self, artist: str) -> Artist:
        cursor = self.database_connector.cursor()
        print(artist)
        query = "SELECT * FROM Artists WHERE title LIKE %s"
        cursor.execute(query, (artist,))

        title = None
        for (id, name, songs, albums) in cursor:
            artist = Artist(name, songs, albums)

        cursor.close()
        return artist
