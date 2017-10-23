from db_connection import MontageDB
from model.encode_image import encode_image
from model.montage.check_person_in_photo import is_in_photo
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class Montage():

    def __init__(self):
        self.montageDB = MontageDB()
        self.all_picture_data = self.montageDB.get_all()

    def add_picture(self, photo_location):
       face_encodings = encode_image(photo_location)
       if len(face_encodings) > 1:
           data = {"photo_location": photo_location,
           "face_encodings": face_encodings}
           self.all_picture_data.append(data)
           self.montageDB.insert_new_picture(photo_location, face_encodings)
           return data
       else:
           return []

    def insert_batch_data_set_from_file(self, picture_file):
        for pic_file in os.listdir(picture_file):
            self.add_picture(pic_file)


    def get_all_photos_with_person_in(self, person_encoding):
        list_of_photos_in = []
        for pic in self.all_picture_data:
            photo_loc = pic["photo_location"]
            distance_of_person = is_in_photo(person_encoding, pic["face_encodings"])
            if distance_of_person:
                list_of_photos_in.append(photo_loc)
        return list_of_photos_in




