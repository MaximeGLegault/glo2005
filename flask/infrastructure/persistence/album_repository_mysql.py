from mysql.connector import MySQLConnection

from domain.album import Album


class AlbumRepositoryMysql:

    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def retrive(self, album_id: int) -> Album:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Albums WHERE album_id = %s"

        cursor.execute(query, (album_id,))

        album = Album()
        for (album_id, artist_id, year, genre_id, title) in cursor:
            album.id = album_id
            album.artist_name = artist_id
            album.year = year
            album.genre = genre_id
            album.title = title

        cursor.close()
        return album
