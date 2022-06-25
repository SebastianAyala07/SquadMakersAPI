from flaskext.mysql import MySQL
import pymysql

mysql = MySQL()

class ConnectionDB:

    connection_instance = None

    @classmethod
    def get_cursor(cls):
        if cls.connection_instance is None:
            cls.connection_instance = mysql.connect()
        cursor = cls.connection_instance.cursor(pymysql.cursors.DictCursor)
        return cls.connection_instance, cursor