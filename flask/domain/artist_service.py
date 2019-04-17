from flask import current_app
from typing import Dict

from domain.artist import Artist

from infrastructure.persistence.artist_repository_mysql import ArtistsRepositoryMySql, ArtistNotFound


class ArtistService:
    def __init__(self):
        self.artist_repository = ArtistsRepositoryMySql(current_app.config["database_connector"])

    def get_Artist(self, artist_id: int) -> Artist:
        return self.artist_repository.get(artist_id)

    def search_artist(self, name):
        try:
            artists = self.artist_repository.search_by_artist_name(name)
        except ArtistNotFound:
            raise ImpossibleToGetArtist("Artist with name %s does not exist".format(name))
        return artists

    def get(self, artist_id: int) -> Artist:
        return self.artist_repository.get_with_album(artist_id)

    def get_all_artists(self):
        return self.artist_repository.get_all_artists()


class ImpossibleToGetArtist(Exception):

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message

    def to_dict(self) -> Dict:
        return {
            "message": self.message,
        }