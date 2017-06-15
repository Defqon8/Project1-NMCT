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
    db=DbConnection
    gegevens1=('SELECT Minutes, Hours FROM TimeOfEnabled')
    gegevens2=('SELECT Minutes, Hours FROM TimeOfDisabled')
    gegevens3=('SELECT Day, Month FROM TimesDisabled')
    gegevens4=('SELECT TimesPerMonth, TimesPerYear FROM TimesAlarmed')
    gegevens5=('SELECT "Alarmed" FROM SystemStatus')
    return render_template('Statistics.html', gegevens1=gegevens1, gegevens2=gegevens2, gegevens3=gegevens3, gegevens4=gegevens4, gegevens5=gegevens5)


@app.route('/Functions')
def functions():
    return render_template('Functions.html')



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=True)
