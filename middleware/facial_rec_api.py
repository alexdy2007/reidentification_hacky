import os
from pathlib import Path
import pickle
import face_recognition

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PICKLE_DIR = CURRENT_DIR + os.sep + ".." + os.sep + "model"
PICTURE_DIR = "{0}{1}..{1}data{1}lfw_funneled".format(CURRENT_DIR, os.sep)
IMAGE_TO_MATCH = "{0}{1}Fernando_Gonzalez{1}Fernando_Gonzalez_0002.jpg".format(PICTURE_DIR, os.sep)
LOAD_FACES_STARTING_WITH = "F"

def get_images_that_are_within(image_to_match=None, distance=0.5):

    if image_to_match is None:
        image_to_match = IMAGE_TO_MATCH


    encoded_list = []
    ids = []
    # Check see if pre-processed pickle verios
    pickle_file_path_images = PICKLE_DIR + os.sep + "pickleImages" + LOAD_FACES_STARTING_WITH + ".pkl"
    pickle_file_path_ids = PICKLE_DIR + os.sep + "pickleIds" + LOAD_FACES_STARTING_WITH + ".pkl"

    pickle_image_file = Path(pickle_file_path_images)
    if pickle_image_file.is_file():
        with open(pickle_file_path_images, 'rb') as f:
            encoded_list = pickle.load(f)
        with open(pickle_file_path_ids, 'rb') as f:
            ids = pickle.load(f)

    # Load a test image and get encondings for it
    image_to_test = face_recognition.load_image_file(image_to_match)
    image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

    # See how far apart the test image is from the known faces
    face_distances = face_recognition.face_distance(encoded_list, image_to_test_encoding)

    names = [list(ids[i].values())[0] for i in range(len(ids))]
    pic_distance = zip(names, face_distances)
    list_to_return = [list(a) for a in pic_distance if a[1]<distance]
    return list_to_return

if __name__ == "__main__":
    get_images_that_are_within()