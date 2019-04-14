from mysql.connector import MySQLConnection

from domain.artist import Artist


class ArtistsRepositoryMySql:

    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def retrive(self, artist_name: str) -> Artist:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Artists WHERE artist_name LIKE %s"
        cursor.execute(query, (artist_name,))

        artist = Artist()
        for (artist_id, artist_name, year_active) in cursor:
            artist.artist_id = artist_id
            artist.name = artist_name
            artist.year_active = year_active
            print(artist.artist_id, artist.name, artist.year_active)

        cursor.close()
        return artist

    def search_by_name(self, name) -> Artist:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Artists WHERE artist_name = %s"

        cursor.execute(query, (name,))

        artist = Artist()
        for (artist_id, artist_name, years_active) in cursor:
            artist.artist_id = artist_id
            artist.name = artist_name
            artist.year_active = years_active
            print(artist_id, artist_name, years_active)

        cursor.close()
        return artist


