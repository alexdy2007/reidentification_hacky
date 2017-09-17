from unittest import TestCase
from sockets.PictureRecSocket import SocketClient
from sockets.PictureRecSocket import SocketClient
from db_connection.Crud import Crud
from model.compare_single_to_known_faces import compare_face_to_known
from model.get_feature_encoded_list import get_feature_encoding_list
import os

class TestPersonSeen(TestCase):

    def setUp(self):
        self.sc = SocketClient()
        self.crud = Crud()

    def test_identify_and_insert_alex(self):
        picture = self.sc.get_picture()
        known_faces = get_feature_encoding_list()
        people_similar = compare_face_to_known(picture, known_faces, True)
        if people_similar is not None:
            most_similar = people_similar[0]
            self.assertEqual(most_similar["name"], "Alex Young")
            self.crud.person_seen_db_insert(most_similar)
            person_seen = self.crud.find_someone_seen_in_last_x_seconds(2)
            self.assertEqual(person_seen[0],"Alex Young")
        else:
            self.fail("No faces found")
