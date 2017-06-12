class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "raspberrypi",
            "user": "pi",
            "passwd": "raspberry",
            "db": "KippenHokdb"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def getTimeOfDisabled(self):
        a = "SELECT TimeOfDisabled.Hours, TimeOfDisabled.Minutes from TimeOfDisabled"  # selecteren
        self.__cursor.execute(a)
        result1 = self.__cursor.fetchall()  # alles die nu geselecteerd is kank vast houden "data ophalen & in result steken"
        self.__cursor.close()
        return result1

    def getTimeOfEnabled(self):
        a = "SELECT TimeOfEnabled.Hours, TimeOfEnabled.Minutes from TimeOfEnabled"  # selecteren
        self.__cursor.execute(a)
        result2 = self.__cursor.fetchall()  # alles die nu geselecteerd is kank vast houden "data ophalen & in result steken"
        self.__cursor.close()
        return result2

    def getTimesalarmed(self):
        a = "SELECT TimesAlarmed.TimesPerYear, TimesAlarmed.TimesPerMonth  from TimesAlarmed"  # selecteren
        self.__cursor.execute(a)
        result3 = self.__cursor.fetchall()  # alles die nu geselecteerd is kank vast houden "data ophalen & in result steken"
        self.__cursor.close()
        return result3

    def getTimesDisabled(self):
        a = "SELECT TimesDisabled.Day, TimesDisabeld.Month from TimesDisabled "  # selecteren
        self.__cursor.execute(a)
        result4 = self.__cursor.fetchall()  # alles die nu geselecteerd is kank vast houden "data ophalen & in result steken"
        self.__cursor.close()
        return result4

    def getImage(self):
        a = "SELECT Snapshots.Snapshotnaam FROM Snapshots"
        self.__cursor.execute(a)
        snapshot = self.__cursor.fetchall()
        self.__cursor.close()
        return snapshot








    # def getDataFromDatabase(self):
    #     # Query zonder parameters
    #     sqlQuery = "SELECT * FROM tabelnaam"
    #
    #     self.__cursor.execute(sqlQuery)
    #     result = self.__cursor.fetchall()
    #     self.__cursor.close()
    #     return result
    #
    #
    # # def getDataFromDatabaseMetVoorwaarde(self, voorwaarde):
    # #     # Query met parameters
    # #     sqlQuery = "SELECT * FROM tablename WHERE columnname = '{param1}'"
    # #     # Combineren van de query en parameter
    # #     sqlCommand = sqlQuery.format(param1=voorwaarde)
    # #
    # #     self.__cursor.execute(sqlCommand)
    # #     result = self.__cursor.fetchall()
    # #     self.__cursor.close()
    # #     return result
    #
    # def setDataToDatabase(self, value1):
    #     # Query met parameters
    #     sqlQuery = "INSERT INTO tablename (columnname) VALUES ('{param1}')"
    #     # Combineren van de query en parameter
    #     sqlCommand = sqlQuery.format(param1=value1)
    #
    #     self.__cursor.execute(sqlCommand)
    #     self.__connection.commit()
    #     self.__cursor.close()