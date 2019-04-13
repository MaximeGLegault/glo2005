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
        for (album_id, title, year, artist_id, genre_id) in cursor:
            album.album_id = album_id
            album.title = title
            album.year = year
            album.artist_id = artist_id
            album.genre_id = genre_id
            print(album.album_id, album.title, album.year, album.artist_id, album.genre_id)
            print(album_id, title, year, artist_id, genre_id)

        cursor.close()
        return album

    def search_by_album_title(self, title: str) -> Album:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Albums WHERE title = %s"

        cursor.execute(query, (title,))

        album = Album()
        for (album_id, artist_id, year, genre_id, title) in cursor:
            album.album_id = album_id
            album.artist_id = artist_id
            album.year = year
            album.genre = genre_id
            album.title = title
            print(album.id, album.artist_id, album.year, album.genre, album.title)

        cursor.close()
        return album

