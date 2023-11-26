import time
import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER_PARASIT = '/resource/image_uploads/parasit'
UPLOAD_FOLDER_NONPARASIT = '/resource/image_uploads/non-parasit'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER_PARASIT'] = UPLOAD_FOLDER_PARASIT
app.config['UPLOAD_FOLDER_NONPARASIT'] = UPLOAD_FOLDER_NONPARASIT
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000 # 16 MiB

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/do_upload_parasit', methods=['POST'])
def upload_file_parasit():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER_PARASIT'], filename))
        return redirect(url_for('download_file_parasit', name=filename))
    
@app.route('/do_upload_nonparasit', methods=['POST'])
def upload_file_nonparasit():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER_NONPARASIT'], filename))
        return redirect(url_for('download_file_nonparasit', name=filename))

@app.route('/uploads/parasit/<name>')
def download_file_parasit(name):
    return send_from_directory(app.config["UPLOAD_FOLDER_PARASIT"], name)

@app.route('/uploads/nonparasit/<name>')
def download_file_nonparasit(name):
    return send_from_directory(app.config["UPLOAD_FOLDER_NONPARASIT"], name)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}