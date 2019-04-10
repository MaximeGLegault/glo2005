from typing import List

from mysql.connector import MySQLConnection

from domain.song import Song


class SongRepositoryMysql:
    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def retrieve(self, song_id: int) -> Song:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Songs WHERE song_id = %s"

        cursor.execute(query, (song_id,))

        song = Song()
        for (song_id, album_id, artist_id, title, duration) in cursor:
            song.song_id = song_id
            song.artist_name = artist_id
            song.albumId = album_id
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
            song.artist_name = artist_id
            song.albumId = album_id
            song.title = title
            song.duration = duration

            songs.append(song)

        cursor.close()
        return songs

