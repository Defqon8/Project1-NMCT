from flask import Flask
from flask import render_template
from dbconn import DbConnection

import os

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('Homepage.html')


@app.route('/Statistics')
def statistics():
    db=DbConnection()
    sql3=("SELECT Minutes, Hours FROM TimeOfEnabled")
    TimeOfEnabled=db.query(sql3)

    sql5=('SELECT Minutes, Hours FROM TimeOfDisabled')
    TimeOfDisabled=db.query(sql5)

    sql1=('SELECT Day, Month FROM TimesDisabled')
    TimesDisabled=db.query(sql1)

    sql9=('SELECT TimesPerMonth, TimesPerYear FROM TimesAlarmed')
    TimesAlarmed=db.query(sql9)

    sql22=('SELECT Alarmed, Enabled, Disabled FROM SystemStatus')
    SystemStatus=db.query(sql22)

    return render_template('Statistics.html', TimeOfEnabled=TimeOfEnabled, TimeOfDisabled=TimeOfDisabled, TimesDisabled=TimesDisabled, TimesAlarmed=TimesAlarmed, SystemStatus=SystemStatus)

# @app.route('/Statistics')
# def statistics():
#     db=DbClass()
#     var = db.get_systemstatus()
#     for i in var:
#         print(i[0])
#         print(i[1])
#     gegevens1=db.get_systemstatus()
#     return render_template('Statistics.html', gegevens1=gegevens1)


@app.route('/Functions')
def functions():
    return render_template('Functions.html')



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=True)
