from flask import Flask
from flask import render_template
from DbClass import DbClass
import os


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('Homepage.html')


@app.route('/Statistics')
def statistics():
    return render_template('Statistics.html')


@app.route('/Functions')
def functions():
    return render_template('Functions.html')


@app.errorhandler(404)
def pagenotfound(error):
    return render_template("error/404.html", error=error)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=True)
