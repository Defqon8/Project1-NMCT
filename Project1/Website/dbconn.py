import mysql.connector as connector
import time
class DbConnection:
    def __init__(self):

        self.__dsn = {
            "host": "169.254.11.12",
            "user": "bram",
            "passwd": "some_pass",
            "db": "KippenHokdb",
        }
        self.__connection = connector.connect(**self.__dsn)
    time.sleep(5)

    # voor lezen (SELECT)
    # met query(..., return_dict=True) krijg je een dictionary terug,
    # dat vermindert de kans op fouten (zeker bij SELECT * FROM..)
    def query(self, query: str, data: dict = None, dictionary=False):
        try:
            cursor = self.__connection.cursor(dictionary=dictionary)
        except TypeError:
            print("Jouw versie van mysql-connector ondersteunt de optie dictionary niet :(")
            cursor = self.__connection.cursor()
        cursor.execute(query, data)
        result = cursor.fetchall()
        cursor.close()
        return result

# voor schrijven (INSERT, UPDATE, ...)
    def execute(self, query: str, data: dict = None):
        cursor = self.__connection.cursor()
        cursor.execute(query, data)
        result = cursor.lastrowid
        self.__connection.commit()
        cursor.close()
        return result

