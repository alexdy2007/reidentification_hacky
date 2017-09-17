
from PIL import Image
import face_recognition

def crop_face_from_image(image_path):
    if isinstance(image_path, str):
        image = face_recognition.load_image_file(image_path)
    else:
        image = image_path
    faces_location = _get_face_locations_from_image(image_path)
    if len(faces_location) != 0:
        faces_location = faces_location[0]
        face_image = image[faces_location[0]:faces_location[2],
                     faces_location[3]:faces_location[1]]
        pil_image = Image.fromarray(face_image,mode="RGB")
        return pil_image
    return None


def _get_face_locations_from_image(image):
    face_locations = face_recognition.face_locations(image)
    return face_locations