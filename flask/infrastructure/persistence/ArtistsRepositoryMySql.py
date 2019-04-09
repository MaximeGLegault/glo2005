from mysql.connector import MySQLConnection

from domain.artist import Artist


class ArtistsRepositoryMySql:

    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def search_by_artist(self, artist: str) -> Artist.name:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Artists WHERE artist_name LIKE %s"
        cursor.execute(query, (artist,))

        artist = None
        for (id, name, year_active) in cursor:
            artist = Artist(name, year_active)

        cursor.close()
        return artist
