from mysql.connector import connect

host = "192.168.99.100"
port = "5000"
username = "root"
password = "1234"
database_name = "glo2005"


def init_bd_mysql(app):
    database_connector = connect(host=host, port=port, user=username, password=password, database=database_name)
    app.config["database_connector"] = database_connector

