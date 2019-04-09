from mysql.connector import MySQLConnection

from domain.song import Song


class SongRepositoryMysql:
    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def retrieve(self, song_id: int) -> Song:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Songs WHERE id = %s"

        cursor.execute(query, (song_id,))

        song = Song()
        for (id, artistName, year, genre, title, duration) in cursor:
            song.id = id
            song.artist_name = artistName
            song.year = year
            song.genre = genre
            song.title = title
            song.duration = duration

        cursor.close()
        return song

    def retrieve_all_from_album(self, album_id):
        pass
