from flask import current_app

from domain.user import User
from infrastructure.jwt_service import JWTService
from infrastructure.password_hasher_brcypt import PasswordHasherBCrypt
from infrastructure.persistence.user_repository_mysql import UserRepositoryMysql


class UserService:
    def __init__(self):
        self.user_repository = UserRepositoryMysql(current_app.config["database_connector"])
        self.password_hasher = PasswordHasherBCrypt()
        self.jwt_service = JWTService()

    def login(self, username: str, password: str) -> User:
        user = self.user_repository.find(username)
        self.password_hasher.check_password_hash(password, user.hashed_password)
        token = self.jwt_service.create_token(user.username)
        return token

    def signup(self, username: str, password: str) -> None:
        is_username_free = self.user_repository.is_username_free(username)
        if not is_username_free:
            raise RuntimeError()

        hashed_password = self.password_hasher.generate_password_hash(password)
        user = User(username, hashed_password)
        self.user_repository.save_new(user)
