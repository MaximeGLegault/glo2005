from mysql.connector import connect

# host = "192.168.99.100"
# host = "localhost"
host = "bd"  # pour le docker-compose
port = "3306"
username = "root"
password = "1234"
database_name = "glo2005"


def init_bd_mysql(app):
    print(host)
    database_connector = connect(host=host, port=port, user=username, password=password, database=database_name)
    app.config["database_connector"] = database_connector

