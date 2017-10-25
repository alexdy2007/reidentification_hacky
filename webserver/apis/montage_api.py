from flask import Blueprint, request, Response
from model.montage.montage import Montage
from werkzeug.utils import secure_filename
import os
from model.montage.create_montage_from_photos import create_montage

montage_page = Blueprint('montage', __name__,
                        template_folder='templates')

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = CURRENT_DIR + os.sep + ".." + os.sep + "static" + os.sep + "tmp" +os.sep

montage = Montage()


@montage_page.route('/api/getmontage', methods=["POST", "OPTIONS"])
def getmontage():

    if 'uploadFile' not in request.files:
        return Response("Can't read or detect image sent", status=502, mimetype='application/json')
    file = request.files['uploadFile']
    filename = secure_filename(file.filename)
    file_path_to_tmp_image = UPLOAD_FOLDER + filename
    file.save(file_path_to_tmp_image)
    photos = montage.get_all_photos_with_person_in(file_path_to_tmp_image)
    create_montage(photos)
    return Response(status=200)
