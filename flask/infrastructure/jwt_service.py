from typing import Tuple

import jwt


class JWTService:
    # todo extract secret, add expiration_date
    ALGORITHM = 'HS256'
    SECRET = "secret"
    USERNAME_FIELD = "username"
    USER_EMAIL_FIELD = "email"
    USER_ID_FIELD = "user_id"

    @staticmethod
    def create_token(username: str, email: str, user_id: int) -> str:
        token = jwt.encode({JWTService.USERNAME_FIELD: username,
                            JWTService.USER_EMAIL_FIELD: email,
                            JWTService.USER_ID_FIELD: user_id},
                           JWTService.SECRET,
                           algorithm=JWTService.ALGORITHM)
        return token.decode("utf-8")

    @staticmethod
    def decode_token(token: str) -> Tuple[str, int]:
        try:
            decoded_jwt = jwt.decode(token, JWTService.SECRET)
            username = decoded_jwt[JWTService.USERNAME_FIELD]
            user_id = decoded_jwt[JWTService.USER_ID_FIELD]
        except Exception:
            raise InvalidToken()

        return username, user_id


class InvalidToken(Exception):
    def __init__(self):
        Exception.__init__(self)
