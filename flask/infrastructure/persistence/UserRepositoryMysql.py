from mysql.connector import MySQLConnection

from domain.user import User


class UserRepositoryMysql:

    def __init__(self, database_connector: MySQLConnection):
        self.database_connector = database_connector

    def find(self, user: str) -> User:
        cursor = self.database_connector.cursor()
        query = "SELECT * FROM Users WHERE username LIKE %s"
        cursor.execute(query, (user,))

        user = None
        for (id, user, first_name, last_name, country, email, hashedPassword) in cursor:
            user = User(user, first_name, last_name, country, email, hashedPassword)

        cursor.close()
        return user

    def save_new(self, user: User) -> None:
        cursor = self.database_connector.cursor()

        query = "INSERT INTO Users (username, first_name, last_name, country, email, hashedPassword) VALUES (%s, %s, %s, %s, %s, %s)"
        data_user = user.username, user.first_name, user.last_name, user.country, user.email, user.hashed_password
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
