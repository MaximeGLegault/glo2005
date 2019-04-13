from flask import current_app

from domain.artist import Artist

from infrastructure.persistence.artist_repository_mysql import ArtistsRepositoryMySql


class ArtistService:
    def __init__(self):
        self.artist_repository = ArtistsRepositoryMySql(current_app.config["database_connector"])

    def get_Artist(self, artist_id: int) -> Artist:
        return self.artist_repository.retrive(artist_id)
