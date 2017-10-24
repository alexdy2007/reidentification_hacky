from unittest import TestCase
from db_connection.Crud import Crud
import os
from model.crop_face_from_image import crop_face_from_image
from model.encode_image import encode_image

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PICTURE_DIR = CURRENT_DIR + os.sep + ".." + os.sep + "pictures" + os.sep
MONTAGE_DIR = CURRENT_DIR + os.sep + ".." + os.sep + ".." + os.sep + "data" + os.sep + "MontageTestData" + os.sep

class TestEncodeImage(TestCase):


    # def test_crop_image(self):
    #     image_path = PICTURE_DIR + "Alex_Young/Alex_Young.jpg"
    #     image = crop_face_from_image(image_path)
    #     image.save("test.jpg", "JPEG", quality=80, optimize=True, progressive=True)

    def test_encode_2_face_in_pic(self):
        pic = MONTAGE_DIR + "stephen_and_laurance.jpg"
        encodings = encode_image(pic)
        print("here")


    def test_1_encode_face_in_pic(self):
        pic = MONTAGE_DIR + "mohit.jpg"
        encodings = encode_image(pic)
        print("HERE")

