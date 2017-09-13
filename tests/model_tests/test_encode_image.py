from unittest import TestCase
from db_connection.Crud import Crud
import os
from model.crop_face_from_image import crop_face_from_image

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PICTURE_DIR = CURRENT_DIR + os.sep + ".." + os.sep + "pictures" + os.sep

class TestEncodeImage(TestCase):


    def test_crop_image(self):
        image_path = PICTURE_DIR + "Alex_Young/Alex_Young.jpg"
        image = crop_face_from_image(image_path)
        image.save("test.jpg", "JPEG", quality=80, optimize=True, progressive=True)


