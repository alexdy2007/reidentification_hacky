import os
from unittest import TestCase
from preprocess.extract_face import get_faces_from_image
from PIL import Image
import face_recognition

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PICTURE_DIR = CURRENT_DIR + os.sep + ".." + os.sep + "pictures" + os.sep


class TestFaceExtractor(TestCase):

    def test_extract_face(self):

        image_path = PICTURE_DIR + "/alex/alex.jpg"
        image = face_recognition.load_image_file(image_path)
        faces_location = get_faces_from_image(image_path)
        faces_location = faces_location[0]
        face_image = image[faces_location[0]:faces_location[2], faces_location[3]:faces_location[1]]
        pil_image = Image.fromarray(face_image)
        pil_image.show()



