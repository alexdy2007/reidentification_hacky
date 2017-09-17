from unittest import TestCase
from sockets.PictureRecSocket import SocketClient
from db_connection.Crud import Crud
from model.compare_single_to_known_faces import compare_face_to_known
from model.crop_face_from_image import crop_face_from_image
from model.get_feature_encoded_list import get_feature_encoding_list
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PICTURE_DIR = CURRENT_DIR + os.sep + ".." + os.sep + "pictures" + os.sep

class TestPictureIdentification(TestCase):

    """
    Inorder for test to pass, must have sight of raspberry pi with facial socket server running
    Alex needs to be standing infont of camera
    """
    def setUp(self):
        self.sc = SocketClient()

    def test_identify_alex(self):
        picture = self.sc.get_picture()
        face = crop_face_from_image(picture)
        known_faces = get_feature_encoding_list()
        people_similar = compare_face_to_known(face, known_faces)
        most_similar = people_similar[0]
        self.assertEqual(most_similar["name"], "Alex Young")


    def test_no_person_found(self):
        picture = self.sc.get_picture()
        face = crop_face_from_image(picture)
        if face is not None:
            known_faces = get_feature_encoding_list()
            people_similar = compare_face_to_known(face, known_faces)
            if len(people_similar) != []:
                most_similar = people_similar[0]
        self.assertEqual(face, None)



