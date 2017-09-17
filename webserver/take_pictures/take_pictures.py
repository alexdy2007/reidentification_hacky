from model.compare_single_to_known_faces import compare_face_to_known
from model.get_feature_encoded_list import get_feature_encoding_list
import time

def take_pictures(sc, crud):
    picture = sc.get_picture()
    known_faces = get_feature_encoding_list()
    people_similar = compare_face_to_known(picture, known_faces, True)
    if people_similar is not None:
        for p in people_similar:
            print("{}:found".format(p["name"]))
            crud.person_seen_db_insert(p)

