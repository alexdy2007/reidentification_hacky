
import face_recognition
import numpy as np

def encode_image(image):
    if isinstance(image, str):
        loaded_image = face_recognition.load_image_file(image)
    else:
        loaded_image = np.array(image)
    person_encoding = face_recognition.face_encodings(loaded_image)
    if len(person_encoding)>0:
        return person_encoding[0]
    else:
        return []