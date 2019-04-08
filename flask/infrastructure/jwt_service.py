import jwt


class JWTService:
    # todo extract secret, add expiration_date
    ALGORITHM = 'HS256'
    SECRET = "secret"
    USERNAME_FIELD = "username"

    @staticmethod
    def create_token(username: str) -> str:
        token = jwt.encode({JWTService.USERNAME_FIELD: username},
                           JWTService.SECRET,
                           algorithm=JWTService.ALGORITHM)
        return token.decode("utf-8")

    @staticmethod
    def decode_token(token: str) -> str:
        try:
            username = jwt.decode(token, JWTService.SECRET)[JWTService.USERNAME_FIELD]
        except Exception:
            raise RuntimeError

        return username
