from flask import Flask, render_template, request, url_for
from markupsafe import escape

app = Flask(__name__)


# hello world
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)
