from unittest import TestCase
from db_connection.Crud import Crud
import os
from model.get_feature_encoded_list import get_feature_encoding_list
from model.compare_single_to_known_faces import compare_face_to_known

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PICTURE_DIR = CURRENT_DIR + os.sep + ".." + os.sep + "pictures" + os.sep

class TestMatchPerson(TestCase):

    def test_person_match(self):

        to_match_pic = CURRENT_DIR + os.sep + "to_match.jpg"
        feature_list = get_feature_encoding_list()
        person_matched = compare_face_to_known(to_match_pic, feature_list)
        first_person_matched = person_matched[0]
        self.assertEqual(first_person_matched["name"], "Alex Young")
