from flask import Flask, send_from_directory, render_template
import flask_resize
import os
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = 'monkey'

app.config['RESIZE_URL'] = 'http://127.0.0.1:5000/'
app.config['RESIZE_ROOT'] = 'static/images'
flask_resize.Resize(app)

@app.route('/')
def index():
    return render_template('image.html')

if __name__ == '__main__':
    app.run(debug=True)