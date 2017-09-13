from unittest import TestCase
from model.crop_face_from_image import crop_face_from_image
from pre_processing.insert_test_data import insert_test_faces_into_db
from pre_processing.encode_test_data import encode_all_people_in_db
from db_connection.Crud import Crud
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PICTURE_DIR = CURRENT_DIR + os.sep + ".." + os.sep + "pictures" + os.sep

class TestEncodeTestImages(TestCase):
    def setUp(self):
        insert_test_faces_into_db()
        self.crud = Crud()

    def test_encode_images(self):
        encode_all_people_in_db()
        person = self.crud.get_person({"name":"AJ Cook"})

        self.assertTrue("encoded_face" in person[0])
        self.assertTrue(len(person[0]["encoded_face"]) > 2)




