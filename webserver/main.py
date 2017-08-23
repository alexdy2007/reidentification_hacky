from flask import Flask, request, redirect, url_for,render_template, jsonify, flash, send_file
import os
from middleware.facial_rec_api import get_images_that_are_within


from werkzeug.utils import secure_filename

CURRENT_DIR =  os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = CURRENT_DIR + os.sep + 'static' + os.sep + "upload"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/comparefile', methods=["POST"])
def comparefile():

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file_path = UPLOAD_FOLDER + os.sep + filename
        name_of_people = get_images_that_are_within(file_path)
        return jsonify(name_of_people)
    else:
        return "NO IMAGE FOUND"

@app.route('/get_image/<filepath>')
def get_image(filepath=None):
    if filepath is None:
        return "NOT FOUND"

    persons_name = filepath.split(os.sep)[-1]
    persons_name = persons_name.split(".")[0]
    filename = CURRENT_DIR + os.sep + ".." + os.sep + "data" + os.sep + "lfw_funneled" + os.sep + persons_name + os.sep + filepath
    return send_file(filename, mimetype='image/gif')

if __name__ == '__main__':
    app.run()
