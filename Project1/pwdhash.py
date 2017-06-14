from Project1.Website import dbconn

day_month = []
minute_hour = []
minute_hour2 = []
month_year = []

parameter1 = 0
parameter2 = 0
parameter3 = 0
parameter4 = 0


# ---------------------------------------------------------------------------------------------------------


def write_TimesDisabled():
    db = dbconn.DbConnection()

    sql1 = ('SELECT TimesDisabled."Day", TimesDisabled."Month" from TimesDisabled')

    TimesAlarmedID = db.query(sql1)

    print(TimesAlarmedID)

    sql2 = (
        'INSERT INTO TimesDisabled (Day, Month) '
        'VALUES ( %(new_Day)s, %(new_Month)s );'
    )

    params1 = {
        'new_day': day_month[0],
        'new_month': day_month[1],
    }

    db.execute(sql2, params1)

    day_month.remove(day_month[0])
    day_month.remove(day_month[0])


def getTimesDisabled(self, params1):
    a = 'SELECT TimesDisabled."Day", TimesDisabled."Month" FROM TimesDisabled'
    self.__cursor.execute(a)
    TimesDisabled = self.__cursor.fetchall()
    self.__cursor.close()
    return TimesDisabled

# ---------------------------------------------------------------------------------------------------------


def write_TimeOfEnabled():
    db = dbconn.DbConnection()

    sql3 = ('SELECT TimeOfEnabled.Minutes, TimeOfEnabled.Hours from TimeOfEnabled')

    TimesAlarmedID = db.query(sql3)

    print(TimesAlarmedID)

    sql4 = (
        'INSERT INTO TimeOfEnabled (Minute, Hour) '
        'VALUES ( %(new_Minute)s, %(new_Hour)s );'
    )

    params2 = {
        'new_minute': minute_hour[0],
        'new_hour': minute_hour[1],
    }

    db.execute(sql4, params2)

    minute_hour.remove(minute_hour[0])
    minute_hour.remove(minute_hour[0])

 # ---------------------------------------------------------------------------------------------------------

def write_TimeOfDisabled():
    db = dbconn.DbConnection()

    sql5 = ('SELECT TimeOfDisabled.Minutes, TimeOfDisabled.Hours from TimeOfDisabled')

    TimesAlarmedID = db.query(sql5)

    print(TimesAlarmedID)

    sql6 = (
        'INSERT INTO TimeOfDisabled (Minute, Hour) '
        'VALUES ( %(new_Minute)s, %(new_Hour)s );'
    )

    params3 = {
        'new_minute': minute_hour2[0],
        'new_hour': minute_hour2[1],
    }

    db.execute(sql6, params3)

    minute_hour2.remove(minute_hour2[0])
    minute_hour2.remove(minute_hour2[0])

 # ---------------------------------------------------------------------------------------------------------

def write_TimeAlarmed():
    db = dbconn.DbConnection()

    sql9 = ('SELECT TimesAlarmed.TimesPerMonth, TimesAlarmed.TimesPerYear from TimesAlarmed')

    TimesAlarmedID = db.query(sql9)

    print(TimesAlarmedID)

    sql10 = (
        'INSERT INTO TimeOfDisabled (Month, Year) '
        'VALUES ( %(new_Month)s, %(new_Year)s );'
    )

    params4 = {
        'new_month': month_year[0],
        'new_year': month_year[1],
    }

    db.execute(sql10, params4)

    month_year.remove(month_year[0])
    month_year.remove(month_year[0])



# ---------------------------------------------------------------------------------------------------------

def write_TimeOfDisabled():
    db = dbconn.DbConnection()

    sql7 = ('SELECT TimeOfDisabled.Minutes, TimeOfDisabled.Hours from TimeOfDisabled')

    TimesAlarmedID = db.query(sql7)

    print(TimesAlarmedID)

    sql8 = (
        'INSERT INTO TimeOfDisabled (Minute, Hour) '
        'VALUES ( %(new_Minute)s, %(new_Hour)s );'
    )

    params4 = {
        'new_minute': minute_hour[0],
        'new_hour': minute_hour[1],
    }

    db.execute(sql8, params4)

    minute_hour.remove(minute_hour[0])
    minute_hour.remove(minute_hour[0])


# ---------------------------------------------------------------------------------------------------------