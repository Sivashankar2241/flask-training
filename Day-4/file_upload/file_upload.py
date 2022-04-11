from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def upload():
    return render_template('file_upload.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        fl = request.files['file1']
        fl.save('uploads/' + fl.filename)
        return render_template('success.html', filename=fl.filename)


if __name__ == '__main__':
    app.run(debug=True)
