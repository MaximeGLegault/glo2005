from mysql.connector import MySQLConnection

from domain.artist import Artist


class ArtistNotFound(Exception):
    pass


class ArtistsRepositoryMySql:

    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def retrive(self, artist_id: int) -> Artist:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Artists WHERE artist_id LIKE %s"
        cursor.execute(query, (artist_id,))

        artist = Artist()
        for (artist_id, artist_name, year_active) in cursor:
            artist.artist_id = artist_id
            artist.name = artist_name
            artist.year_active = year_active

        cursor.close()
        return artist

    def search_by_artist_name(self, artist_name):
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Artists WHERE artist_name LIKE '%"+artist_name+"%'"

        cursor.execute(query)

        results = cursor.fetchall()

        if cursor.rowcount == 0:
            cursor.close()
            raise ArtistNotFound()

        artists = []
        for row in results:
            artist = Artist()
            artist.artist_id = row[0]
            artist.artist_name = row[1]
            artist.year_active = row[2]
            artists.append(artist)


        cursor.close()
        return artists

    def get_all_artists(self):
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Artists"

        cursor.execute(query)

        results = cursor.fetchall()

        if cursor.rowcount == 0:
            cursor.close()
            raise ArtistNotFound()

        artists = []
        for row in results:
            artist = Artist()
            artist.artist_id = row[0]
            artist.artist_name = row[1]
            artist.year_active = row[2]
            artists.append(artist)

        cursor.close()
        return artists

