from mysql.connector import MySQLConnection

from domain.album import Album
from domain.song import Song


class AlbumNotFound(Exception):
    pass

class AlbumRepositoryMysql:

    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def retrive(self, album_id: int) -> Album:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Albums WHERE album_id = %s"

        cursor.execute(query, (album_id,))

        album = Album()
        (album_id, title, year, artist_id, genre_id) = cursor.fetchone()
        album.album_id = album_id
        album.artist_id = artist_id
        album.year = year
        album.genre_id = genre_id
        album.title = title

        query = "SELECT genre_name FROM Genres WHERE genre_id = %s"
        cursor.execute(query, (album.genre_id,))
        genre_name, = cursor.fetchone()
        album.genre_name = genre_name

        query = "SELECT artist_name FROM Artists WHERE artist_id = %s"
        cursor.execute(query, (album.artist_id,))
        artist_name, = cursor.fetchone()
        album.artist_name = artist_name

        query = "SELECT * FROM Songs WHERE album_id = %s"
        cursor.execute(query, (album_id,))
        songs = []
        for (song_id, album_id, artist_id, title, duration) in cursor:
            song = Song()
            song.song_id = song_id
            song.artist_id = artist_id
            song.artist_name = album.artist_name
            song.album_id = album.album_id
            song.album_name = album.title
            song.title = title
            song.duration = duration
            song.genre_id = album.genre_id
            song.genre_name = album.genre_name

            songs.append(song)

        cursor.close()

        album.songs = songs
        return album

    def search_by_album_title(self, title: str) -> Album:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Albums WHERE title = %s"

        cursor.execute(query, (title,))

        results = cursor.fetchone()

        if results is None:
            print("result is none")
            cursor.close()
            raise AlbumNotFound()

        album = Album()
        album_id, title, year, artist_id, genre_id = results
        album.album_id = album_id
        album.title = title
        album.year = year
        album.artist_id = artist_id
        album.genre_id = genre_id

        query = "SELECT genre_name FROM Genres WHERE genre_id = %s"
        cursor.execute(query, (album.genre_id,))
        genre_name, = cursor.fetchone()
        album.genre_name = genre_name

        query = "SELECT artist_name FROM Artists WHERE artist_id = %s"
        cursor.execute(query, (album.artist_id,))
        artist_name, = cursor.fetchone()
        album.artist_name = artist_name

        query = "SELECT * FROM Songs WHERE album_id = %s"
        cursor.execute(query, (album_id,))
        songs = []
        for (song_id, album_id, artist_id, title, duration) in cursor:
            song = Song()
            song.song_id = song_id
            song.artist_id = artist_id
            song.artist_name = album.artist_name
            song.album_id = album.album_id
            song.album_name = album.title
            song.title = title
            song.duration = duration
            song.genre_id = album.genre_id
            song.genre_name = album.genre_name

            songs.append(song)

        cursor.close()

        album.songs = songs
        return album

