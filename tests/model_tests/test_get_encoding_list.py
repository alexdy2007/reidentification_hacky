from unittest import TestCase
from db_connection.Crud import Crud
import os
from model.get_feature_encoded_list import get_feature_encoding_list

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PICTURE_DIR = CURRENT_DIR + os.sep + ".." + os.sep + "pictures" + os.sep

class TestGetEncodedListOfKnownPeople(TestCase):

    def test_list_of_known_people(self):
        feature_list = get_feature_encoding_list()
        self.assertTrue(len(feature_list)==2)
        feature_with_name = tuple(zip(feature_list[0],feature_list[1]))
        self.assertTrue(len(feature_with_name)>40)




