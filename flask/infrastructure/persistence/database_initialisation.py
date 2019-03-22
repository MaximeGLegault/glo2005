from mysql.connector import connect

host = "localhost"
port = "6033"
username = "root"
password = "1234"
database_name = "glo2005"


def init_bd_mysql(app):
    database_connector = connect(host=host, port=port, user=username, password=password, database=database_name)
    app.config["database_connector"] = database_connector

