from mysql.connector import MySQLConnection

from domain.user import User


class UserRepositoryMysql:

    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def find_username(self, user: str) -> User:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Users WHERE username LIKE %s"
        cursor.execute(query, (user,))

        user = None
        for (id, user, email, hashedPassword) in cursor:
            user = User(user, email, hashedPassword)

        cursor.close()
        return user

    def find_email(self, user: str) -> User:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Users WHERE email LIKE %s"
        cursor.execute(query, (user,))

        user = None
        for (id, user, email, hashedPassword) in cursor:
            user = User(user, email, hashedPassword)

        cursor.close()
        return user

    def save_new(self, user: User) -> None:
        cursor = self.database_connector.cursor()

        query = "INSERT INTO Users (username, email, hashedPassword) VALUES (%s, %s, %s)"
        data_user = user.username, user.email, user.hashed_password
        cursor.execute(query, data_user)

        self.database_connector.commit()
        cursor.close()

    def is_username_free(self, username):
        cursor = self.database_connector.cursor()

        query = "SELECT COUNT(username) FROM Users WHERE username = %s"
        cursor.execute(query, (username, ))
        (number_of_rows,) = cursor.fetchone()
        if number_of_rows > 0:
            return False

        return True

    def is_email_free(self, email):
        cursor = self.database_connector.cursor()

        query = "SELECT COUNT(email) FROM Users WHERE email = %s"
        cursor.execute(query, (email, ))
        (number_of_rows,) = cursor.fetchone()
        if number_of_rows > 0:
            return False

        return True
