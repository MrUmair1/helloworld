from idlelib import __main__

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hellow():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
