class DbClass:
    def __init__(self):
        import mysql.connector as connector
        self.__dsn = {
            "host": "169.254.11.12",
            "user": "bram",
            "passwd": "some_pass",
            "db": "KippenHokdb"
        }
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def get_systemstatus(self):
        qGebruiker = "select * from TimesAlarmed ;"
        self.__cursor.execute(qGebruiker)
        resultGebruiker = self.__cursor.fetchall()
        return resultGebruiker