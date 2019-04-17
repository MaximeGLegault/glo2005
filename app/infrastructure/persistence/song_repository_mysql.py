from typing import List

from mysql.connector import MySQLConnection

from domain.song import Song

class SongNotFound(Exception):
    pass

class SongRepositoryMysql:
    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def retrieve(self, song_id: int) -> Song:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Songs WHERE song_id = %s"

        cursor.execute(query, (song_id,))

        song = Song()
        song_id, album_id, artist_id, title, duration = cursor.fetchone()
        song.song_id = song_id
        song.artist_name = artist_id
        song.album_id = album_id
        song.title = title
        song.duration = duration

        cursor.close()
        return song

    def retrieve_all_from_album(self, album_id) -> List[Song]:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Songs WHERE album_id = %s"

        cursor.execute(query, (album_id,))

        songs = []
        for (song_id, album_id, artist_id, title, duration) in cursor:
            song = Song()
            song.song_id = song_id
            song.artist_id = artist_id
            song.album_id = album_id
            song.title = title
            song.duration = duration

            songs.append(song)

        cursor.close()
        return songs

    def search_by_title(self, title_song):
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Songs WHERE title LIKE '%"+title_song+"%'"

        cursor.execute(query)

        results = cursor.fetchall()

        if cursor.rowcount == 0:
            cursor.close()
            raise SongNotFound()

        songs = []
        for row in results:
            song = Song()
            song.song_id = row[0]
            song.album_id = row[1]
            song.artist_id = row[2]
            song.title = row[3]
            song.duration = row[4]
            songs.append(song)

        for song in songs:
            query = "SELECT title FROM Albums WHERE album_id = %s"
            cursor.execute(query, (song.album_id,))
            album_name = cursor.fetchone()
            song.album_name = album_name[0]

            query = "SELECT artist_name FROM Artists WHERE artist_id = %s"
            cursor.execute(query, (song.artist_id,))
            artist_name = cursor.fetchone()
            song.artist_name = artist_name[0]

        cursor.close()
        return songs

    def get_all_songs(self):

        cursor = self.database_connector.cursor()

        query = "SELECT * FROM Songs"

        cursor.execute(query)

        results = cursor.fetchall()

        if cursor.rowcount == 0:
            cursor.close()
            raise SongNotFound()

        songs = []
        for row in results:
            song = Song()
            song.song_id = row[0]
            song.album_id = row[1]
            song.artist_id = row[2]
            song.title = row[3]
            song.duration = row[4]
            songs.append(song)

        for song in songs:
            query = "SELECT title FROM Albums WHERE album_id = %s"
            cursor.execute(query, (song.album_id,))
            album_name = cursor.fetchone()
            song.album_name = album_name[0]

            query = "SELECT artist_name FROM Artists WHERE artist_id = %s"
            cursor.execute(query, (song.artist_id,))
            artist_name = cursor.fetchone()
            song.artist_name = artist_name[0]

        cursor.close()
        return songs

