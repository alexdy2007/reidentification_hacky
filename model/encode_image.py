
import face_recognition
import numpy as np

def encode_image(image):
    """
    :param image: srt file location or np.array
    :return: [[int,int,..],[int,int,...],...]
    """
    if isinstance(image, str):
        loaded_image = face_recognition.load_image_file(image)
    else:
        loaded_image = np.array(image)
    people_encoding = face_recognition.face_encodings(loaded_image)
    if len(people_encoding)>0:
        return people_encoding
    else:
        return []