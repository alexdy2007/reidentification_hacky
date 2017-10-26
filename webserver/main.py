from flask import Flask, request, jsonify, Response
import os
from webserver.person.person import Person
from flask_restful import Api
import threading
from werkzeug.utils import secure_filename
from webserver.take_pictures.take_pictures import take_pictures
from db_connection.PeopleDB import PeopleDB
from db_connection.MontageDB import MontageDB
from time import sleep
from webserver.apis.montage_api import montage_page
from sockets.PictureRecSocket import SocketClient
from model.montage.montage import Montage

CURRENT_DIR =  os.path.dirname(os.path.realpath(__file__))
DATA_DIR = CURRENT_DIR + os.sep + ".."  + os.sep + "data" + os.sep
PICTURE_DIR = CURRENT_DIR + os.sep + ".." + os.sep + "webface" + os.sep + "src" + os.sep + "assets" + os.sep + "pictures" + os.sep

UPLOAD_FOLDER = PICTURE_DIR
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

TIME_BETWEEN_PICTURES = 4
PEOPLE_VIS_IN_LAST_SECS = 12

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.register_blueprint(montage_page)
api = Api(app)
api.add_resource(Person,"/api")

peopleDB = PeopleDB()
montageDB = MontageDB()
montage = Montage()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/comparefile', methods=["POST"])
def comparefile():

    if 'file' not in request.files:
        return Response("Can't read or detect image sent", status=502, mimetype='application/json')

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file_path = UPLOAD_FOLDER + os.sep + filename
    else:
        return "NO IMAGE FOUND"

@app.route('/api/addperson', methods=["POST", "OPTIONS"])
def addperson():

    def count_current_photos_of_person(person_dir):
        dir_to_check = PICTURE_DIR + person_dir

        if not os.path.exists(dir_to_check):
            os.makedirs(dir_to_check)

        number_of_photos_of_person = len(os.listdir(dir_to_check))
        n = number_of_photos_of_person + 1
        n_str = str(n)
        if n < 10:
            prefix = "000" + n_str
        else:
            prefix = "00" + n_str
        return prefix


    if 'uploadFile' not in request.files:
        return Response("Can't read or detect image sent", status=502, mimetype='application/json')
    first_name = request.values["name"].capitalize()
    last_name = request.values["lastName"].capitalize()
    if request.values["role"] == "":
        role = "Not Specified"
    else:
        role = request.values["role"].capitalize()

    file = request.files['uploadFile']
    file_name = file.filename
    file_type = file_name.split(".")[1]
    folder_dir = first_name + "_" + last_name

    if file and allowed_file(file_name):
        n = count_current_photos_of_person(folder_dir)
        new_file_name = first_name + "_" + last_name + "_" + n + "." + file_type
        filename = secure_filename(new_file_name)
        final_path = folder_dir + os.sep + filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], final_path))

        person_data = {
            "name": folder_dir,
            "role": role,
            "photo_location": PICTURE_DIR + final_path,
            "has_encodings": False
        }

        peopleDB.insert_person(person_data)

    print("OK")
    return "Success"

@app.route('/api/peoplevisable', methods=["GET"])
def peoplevisable():
    people_seen = peopleDB.find_someone_seen_in_last_x_seconds(PEOPLE_VIS_IN_LAST_SECS)
    if len(people_seen)!=0:
        query = {"name": {'$in':people_seen}}
        people_profiles = peopleDB.get_person(query)
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
        make_montage = True
        take_pictures(sc, crud, montage, make_montage)
        sleep(2)



if __name__ == '__main__':
    # run_web()
    threads = []
    sc = SocketClient()
    t1 = threading.Thread(target=repeat_picture_capture, args=(sc,peopleDB))
    t2 = threading.Thread(target=run_web)
    threads.append(t1)
    threads.append(t2)
    for t in threads:
        t.start()
    while True:
        pass

