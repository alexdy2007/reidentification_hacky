from model.montage.montage import Montage
from unittest import TestCase
import os
from model.crop_face_from_image import crop_face_from_image

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PICTURE_DIR = CURRENT_DIR + os.sep + ".." + os.sep + ".." + os.sep + "data" + os.sep + "MontageTestData"

class TestMontage(TestCase):

    def setUp(self):
        self.montage = Montage()

    def test_add_to_montage_db(self):
        image = crop_face_from_image(image_path)
        image.save("test.jpg", "JPEG", quality=80, optimize=True, progressive=True)


