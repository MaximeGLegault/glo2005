from mysql.connector import MySQLConnection

from domain.album import Album


class AlbumRepositoryMysql:

    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def retrive(self, album_id: int) -> Album:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Albums WHERE id = %s"

        cursor.execute(query, (album_id,))

        album = Album()
        for (id, artistName, year, genre, title, description) in cursor:
            album.id = id
            album.artist_name = artistName
            album.year = year
            album.genre = genre
            album.title = title
            album.description = description

        cursor.close()
        return album
