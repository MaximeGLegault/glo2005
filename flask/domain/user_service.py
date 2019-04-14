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

    def login(self, username: str, password: str) -> str:
        user = self.user_repository.find_username(username)
        self.password_hasher.check_password_hash(password, user.hashed_password)
        token = self.jwt_service.create_token(user.username, user.email)

        return token

    def signup(self, username: str, email: str, password: str) -> str:
        is_username_free = self.user_repository.is_username_free(username)
        if not is_username_free:
            raise ConflictSignup("username already exist")
        is_email_free = self.user_repository.is_email_free(email)
        if not is_email_free:
            raise ConflictSignup("email is already in use")
        hashed_password = self.password_hasher.generate_password_hash(password)
        user = User(username, email, hashed_password)
        self.user_repository.save_new(user)
        token = self.jwt_service.create_token(user.username, user.email)

        return token


class ConflictSignup(Exception):
    status_code = 409

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
