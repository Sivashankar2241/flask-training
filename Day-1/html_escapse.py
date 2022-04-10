from flask import Flask, escape

app = Flask(__name__)


# html escape
@app.route('/<name>')
def html_escape(name):
    return f"Hello, {escape(name)}!"


if __name__ == '__main__':
    app.run(debug=True)
