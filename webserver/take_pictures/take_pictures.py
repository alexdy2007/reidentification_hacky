from model.compare_single_to_known_faces import compare_face_to_known
from model.get_feature_encoded_list import get_feature_encoding_list
from model.montage.create_montage_from_photos import create_montage
from PIL import Image
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = CURRENT_DIR + os.sep + ".." + os.sep + "static" + os.sep + "tmp" +os.sep
TEMP_FILE = UPLOAD_FOLDER + "tmpstream.jpg"

def take_pictures(sc, crud, create_montage=False):
    picture = sc.get_picture()
    known_faces = get_feature_encoding_list()
    people_similar = compare_face_to_known(picture, known_faces, True)
    if people_similar is not None:
        for p in people_similar:
            print("{}:found".format(p["name"]))
            crud.person_seen_db_insert(p)
    if create_montage:
        im = Image.fromarray(picture)
        im.save(TEMP_FILE)
        create_montage(TEMP_FILE)
