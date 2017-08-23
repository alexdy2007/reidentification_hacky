from pre_processing.get_faces import get_faces
import face_recognition
import os
import pickle
from pathlib import Path


CURRENT_DIR =  os.path.dirname(os.path.realpath(__file__))
PICTURE_DIR = "{0}{1}..{1}data{1}lfw_funneled".format(CURRENT_DIR, os.sep)

IMAGE_TO_MATCH = "{0}{1}Fernando_Gonzalez{1}Fernando_Gonzalez_0002.jpg".format(PICTURE_DIR, os.sep)

LOAD_FACES_STARTING_WITH = "F"

def contruct_encoded_images_of_people(people, image_to_match=None, precompiled=True):

    # Encoding Part
    image_to_match = IMAGE_TO_MATCH
    encoded_list = []
    ids = []
    # Check see if pre-processed pickle verios
    pickle_file_path_images = CURRENT_DIR + os.sep + "pickleImages" + LOAD_FACES_STARTING_WITH + ".pkl"
    pickle_file_path_ids = CURRENT_DIR + os.sep + "pickleIds" + LOAD_FACES_STARTING_WITH + ".pkl"

    pickle_image_file = Path(pickle_file_path_images)
    if pickle_image_file.is_file() and precompiled:
        with open(pickle_file_path_images, 'rb') as f:
            encoded_list = pickle.load(f)
        with open(pickle_file_path_ids, 'rb') as f:
            ids = pickle.load(f)

    else:
        person_count = 0
        for name, images in people.items():
            person_file_path = PICTURE_DIR + os.sep + name + os.sep
            for image_name in images:
                person_file_path_specific = person_file_path + image_name
                if person_file_path_specific != IMAGE_TO_MATCH:
                    person_image = face_recognition.load_image_file(person_file_path_specific)
                    try:
                        person_encoding = face_recognition.face_encodings(person_image)[0]
                        encoded_list.append(person_encoding)
                        ids.append({person_count: person_file_path_specific.split(os.sep)[-1]})
                        person_count += 1
                        print("encoded : {}".format(person_file_path_specific))
                    except IndexError:
                        print("ERROR for : {}".format(person_file_path_specific))
        #PICKEL ENCODINGS FOR LATER USE
        with open(pickle_file_path_images, 'wb') as f:
            _ = pickle.dump(encoded_list, f)
        with open(pickle_file_path_ids, 'wb') as f:
            _ = pickle.dump(ids, f)



    # Load a test image and get encondings for it
    image_to_test = face_recognition.load_image_file(image_to_match)
    image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

    # See how far apart the test image is from the known faces
    face_distances = face_recognition.face_distance(encoded_list, image_to_test_encoding)


    for i, face_distance in enumerate(face_distances):
        if face_distance < 0.6:
            print("The test image has a distance of {:.2} from known image #{}".format(face_distance, ids[i]))
            print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
            print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
            print()

if __name__ == "__main__":
    people = get_faces(LOAD_FACES_STARTING_WITH)
    contruct_encoded_images_of_people(people)
