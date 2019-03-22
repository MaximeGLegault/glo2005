from flask import current_app


class PasswordHasherBCrypt:
    def __init__(self):
        self.bcrypt = current_app.config["hasher"]

    def generate_password_hash(self, password: str) -> str:
        return self.bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password_hash(self, password: str, password_hash: str) -> bool:
        return self.bcrypt.check_password_hash(password, password_hash)
