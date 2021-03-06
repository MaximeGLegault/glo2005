from typing import List

from mysql.connector import MySQLConnection

from domain.playlist import Playlist
from domain.song import Song


class PlaylistNotFound(Exception):
    pass


class PlaylistRepositoryMysql:
    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def get_playlist_from_username(self, user_id: int) -> List[Playlist]:
        cursor = self.database_connector.cursor()
        query = "SELECT p.playlist_id, p.title FROM Playlists p, Users_Playlists up WHERE p.playlist_id = " \
                "up.playlist_id AND up.user_id = %s"
        cursor.execute(query, (user_id,))

        playlists = []
        for playlist_id, title in cursor:
            playlist = Playlist()
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

        results = cursor.fetchone()

        if results is None:
            cursor.close()
            raise PlaylistNotFound()

        playlist_id, title = results
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

        cursor.nextset()
        cursor.close()
        return playlist

    def delete(self, playlist_id):
        cursor = self.database_connector.cursor()

        query = "DELETE FROM Users_Playlists WHERE playlist_id = %s"
        cursor.execute(query, (playlist_id,))

        query = "DELETE FROM Playlists WHERE playlist_id = %s"
        cursor.execute(query, (playlist_id,))

        self.database_connector.commit()
        cursor.close()

    def is_playlist_by_user(self, user_id: str, playlist_id: int):
        cursor = self.database_connector.cursor()

        query = "SELECT COUNT(*) FROM Users_Playlists WHERE user_id = %s AND playlist_id = %s"
        cursor.execute(query, (user_id, playlist_id))

        # should have on if exists
        number_of_row, = cursor.fetchone()

        cursor.close()
        return number_of_row > 0

    def add_playlist_to_user(self, user_id: int, title: str) -> int:
        playlist_id = self.add(title)
        self.link(user_id, playlist_id)

        return playlist_id

    def add_song_to_playlist(self, playlist_id, song_id):
        cursor = self.database_connector.cursor()

        query = "SELECT * FROM Playlist_Songs WHERE playlist_id = %s AND song_id = %s"
        cursor.execute(query, (playlist_id, song_id))

        results = cursor.fetchone()

        if results is not None:
            cursor.close()
            return playlist_id

        query = "INSERT INTO Playlist_Songs (playlist_id, song_id) VALUES (%s, %s)"
        cursor.execute(query, (playlist_id, song_id))

        self.database_connector.commit()
        cursor.close()
        return playlist_id

    def delete_song(self, playlist_id, song_id):
        cursor = self.database_connector.cursor()

        query = "DELETE FROM Playlist_Songs WHERE song_id = %s AND playlist_id = %s"
        cursor.execute(query, (song_id,playlist_id))

        self.database_connector.commit()
        cursor.close()

    def add_to_history(self,user_id,song_id):
        playlist_id= self.history_exists(user_id);
        if(playlist_id>=0):
            self.add_song_to_playlist(playlist_id,song_id)
        else:
            id = self.add_playlist_to_user(user_id,"History")
            self.add_song_to_playlist(id,song_id)
        return song_id

    def like_song(self,user_id,song_id):
        playlist_id= self.liked_playlist_exists(user_id);
        if(playlist_id>=0):
            self.add_song_to_playlist(playlist_id,song_id)
        else:
            id = self.add_playlist_to_user(user_id,"Liked")
            self.add_song_to_playlist(id,song_id)
        return song_id

    def liked_playlist_exists(self,user_id):
        playlist_id = -1
        playlists = self.get_playlist_from_username(user_id)

        for play in playlists:
            if(play.title == "Liked"):
                playlist_id=play.playlist_id
                break

        return playlist_id

    def history_exists(self,user_id):
        playlist_id = -1
        playlists = self.get_playlist_from_username(user_id)

        for play in playlists:
            if(play.title == "History"):
                playlist_id=play.playlist_id
                break

        return playlist_id

    def unlike_song(self,user_id,song_id):
        playlist_id= self.liked_playlist_exists(user_id);
        if(playlist_id>=0):
            self.delete_song(playlist_id,song_id)
        else:
            song_id = -1
        return song_id

    def add(self, title) -> int:
        cursor = self.database_connector.cursor()

        query = "INSERT INTO Playlists (title) VALUES (%s)"
        cursor.execute(query, (title,))

        self.database_connector.commit()

        playlist_id = cursor.lastrowid
        cursor.close()

        return playlist_id

    def link(self, user_id: int, playlist_id: int) -> None:
        cursor = self.database_connector.cursor()

        query = "INSERT INTO Users_Playlists (user_id, playlist_id) VALUES (%s, %s)"
        cursor.execute(query, (user_id, playlist_id))

        self.database_connector.commit()
        cursor.close()
