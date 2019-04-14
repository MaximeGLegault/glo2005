from typing import List

from mysql.connector import MySQLConnection

from domain.Playlist import Playlist
from domain.song import Song


class PlaylistRepositoryMysql:
    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def get_playlist_from_username(self, username: str) -> List[Playlist]:
        cursor = self.database_connector.cursor()
        query = "SELECT id FROM Users WHERE username = %s"

        cursor.execute(query, (username,))
        user_id,  = cursor.fetchone()

        query = "SELECT p.playlist_id, p.title FROM Playlists p, Users_Playlists up WHERE p.playlist_id = " \
                "up.playlist_id AND up.user_id = %s"
        cursor.execute(query, (user_id,))

        playlists = []
        for playlist_id, title in cursor:
            playlist = Playlist()
            playlist.user_username = username
            playlist.user_id = user_id
            playlist.playlist_id = playlist_id
            playlist.title = title

            playlists.append(playlist)

        cursor.close()
        return playlists

    def get(self, playlist_id: int) -> Playlist:
        cursor = self.database_connector.cursor()

        query = "SELECT * FROM Playlists WHERE playlist_id = %s"
        cursor.execute(query, (playlist_id,))

        playlist_id, title = cursor.fetchone()
        playlist = Playlist()
        playlist.playlist_id = playlist_id
        playlist.title = title

        query = "SELECT user_id FROM Users_Playlists WHERE playlist_id = %s"
        cursor.execute(query, (playlist_id,))

        user_id, = cursor.fetchone()
        playlist.user_id = user_id

        query = "SELECT s.song_id, s.album_id, s.artist_id, s.title, s.duration FROM Songs s, Playlist_Songs ps WHERE " \
                "s.song_id = ps.song_id AND ps.playlist_id = %s"
        cursor.execute(query, (playlist_id, ))

        for (song_id, album_id, artist_id, title, duration) in cursor:
            song = Song()
            song.song_id = song_id
            song.artist_id = artist_id
            song.album_id = album_id
            song.title = title
            song.duration = duration

            playlist.songs.append(song)

        for song in playlist.songs:
            query = "SELECT artist_name FROM Artists WHERE artist_id = %s"
            cursor.execute(query, (song.artist_id,))
            artist_name, = cursor.fetchone()
            song.artist_name = artist_name

        for song in playlist.songs:
            query = "SELECT title FROM Albums WHERE album_id = %s"
            cursor.execute(query, (song.album_id,))
            title, = cursor.fetchone()
            song.album_name = title

        cursor.close()
        return playlist
