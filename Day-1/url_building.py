from flask import Flask, redirect, url_for

app = Flask(__name__)


# url redirection
@app.route('/adm')
def admin():
    return "<h1>admin here...<h1>"


@app.route('/doc')
def doctor():
    return "<h1>doctor...</h1>"


@app.route('/pat')
def patient():
    return '<h1>patient...</h1>'


@app.route('/user/<name>')
def user(name):
    if name == 'adm':
        redirect(url_for('adm'))
    if name == 'doc':
        redirect(url_for('doc'))
    if name == 'pat':
        redirect(url_for('pat'))


if __name__ == '__main__':
    app.run(debug=True)
