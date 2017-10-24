from model.montage.montage import Montage
from unittest import TestCase
import os
from model.montage.create_montage_from_photos import create_montage
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PICTURE_TEST_DIR = CURRENT_DIR + os.sep + ".." + os.sep + ".." + os.sep + ".." + os.sep + "data" + os.sep + "MontageTestData" + os.sep

class TestMontage(TestCase):

    def setUp(self):
        self.montage = Montage()

    def test_add_to_montage_db(self):
        self.montage.delete_all()
        self.montage.insert_batch_data_set_from_file(PICTURE_TEST_DIR)
        pics = self.montage.get_all()
        self.assertEquals(len(pics), 16)

    def test_mat_returns_2_pics(self):
        matt_pic_file = CURRENT_DIR + os.sep + "Matt_glasses.jpg"
        photos = self.montage.get_all_photos_with_person_in(matt_pic_file)
        print(photos)
        self.assertEquals(len(photos), 4)


    def test_create_montage_matt(self):
        matt_pic_file = CURRENT_DIR + os.sep + "Matt_glasses.jpg"
        photos = self.montage.get_all_photos_with_person_in(matt_pic_file)
        print(photos)
        create_montage(photos)

    def test_create_montage_frank(self):
        frank_pic_file = CURRENT_DIR + os.sep + "frank2.jpg"
        photos = self.montage.get_all_photos_with_person_in(frank_pic_file)
        print(photos)
        create_montage(photos)

    def test_create_montage_alex(self):
        alex_pic_file = CURRENT_DIR + os.sep + "alex.jpg"
        photos = self.montage.get_all_photos_with_person_in(alex_pic_file)
        print(photos)
        create_montage(photos)