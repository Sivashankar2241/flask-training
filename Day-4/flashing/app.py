
from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)
app.secret_key = 'sdfjsdfV2q6qsfd@j_sdfjdsf180SDFSfjsdfunsddqpasnsdf'


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] != '123':
            error = 'Invalid password'
        else:
            flash('you are logged in successfully!')
            return redirect(url_for('home'))

    return render_template('login.html', error=error)


@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
