import sqlite3
from flask import Flask, render_template


app = Flask(__name__)

app.config.from_envvar('FLASK_CONFIG')


@app.route('/')
def hello_world():
    return render_template('hello.html', debug=app.config['DEBUG'])


if __name__ == '__main__':
    app.run(host="0.0.0.0")
