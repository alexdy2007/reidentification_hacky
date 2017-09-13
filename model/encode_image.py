
import face_recognition

def encode_image(image):
    loaded_image = face_recognition.load_image_file(image)
    person_encoding = face_recognition.face_encodings(loaded_image)
    if len(person_encoding)>0:
        return person_encoding[0]
    else:
        return []