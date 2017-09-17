from flask import Flask, request, redirect, flash, jsonify
import os
from webserver.person.person import Person
from flask_restful import Api
import threading
from werkzeug.utils import secure_filename
from webserver.take_pictures.take_pictures import take_pictures
from sockets.PictureRecSocket import SocketClient
from db_connection.Crud import Crud
from time import sleep
from pathlib import Path

CURRENT_DIR =  os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = CURRENT_DIR + os.sep + 'static' + os.sep + "upload"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

TIME_BETWEEN_PICTURES = 4
PEOPLE_VIS_IN_LAST_SECS = 12

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)
api.add_resource(Person,"/api")
crud = Crud()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
    else:
        return "NO IMAGE FOUND"

@app.route('/api/peoplevisable', methods=["GET"])
def peoplevisable():
    people_seen = crud.find_someone_seen_in_last_x_seconds(PEOPLE_VIS_IN_LAST_SECS)
    if len(people_seen)!=0:
        query = {"name": {'$in':people_seen}}
        people_profiles = crud.get_person(query)
        for p in people_profiles:
            if "encoded_face" in p: del p["encoded_face"]
            del p["_id"]
            if "photo_location" in p:
                split_path = p["photo_location"].split("/")
                split_pt = split_path.index("assets")
                p["photo_location"] =  "/".join(split_path[split_pt:])
        return jsonify(people_profiles)
    else:
        return jsonify([])



def run_web():
    app.run()

def repeat_picture_capture(sc, crud):
    while True:
        take_pictures(sc, crud)
        sleep(2)



if __name__ == '__main__':
    threads = []
    sc = SocketClient()
    t1 = threading.Thread(target=repeat_picture_capture, args=(sc,crud))
    t2 = threading.Thread(target=run_web)
    threads.append(t1)
    threads.append(t2)
    for t in threads:
        t.start()
    while True:
        pass

