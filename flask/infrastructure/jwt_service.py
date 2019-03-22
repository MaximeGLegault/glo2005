import jwt


class JWTService:
    # todo extract secret, add expiration_date
    ALGORITHM = 'HS256'
    SECRET = "secret"

    @staticmethod
    def create_token(username: str) -> str:
        return jwt.encode({username: username}, JWTService.SECRET, algorithm=JWTService.ALGORITHM)

    @staticmethod
    def decode_token(token: str) -> str:
        return jwt.decode(token, JWTService.SECRET)
