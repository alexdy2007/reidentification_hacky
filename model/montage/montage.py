from db_connection.MontageDB import MontageDB
from model.encode_image import encode_image
from model.montage.check_person_in_photo import is_in_photo
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
SAVE_FILE = CURRENT_DIR

class Montage():

    def __init__(self):
        self.montageDB = MontageDB()
        self.all_picture_data = self.montageDB.get_all()
        self.save_file = SAVE_FILE

    def add_picture(self, photo_location):
       face_encodings = encode_image(photo_location)
       print("people found {}".format(len(face_encodings)))
       if len(face_encodings) > 0:
           data = {"photo_location": photo_location,
           "face_encodings": face_encodings}
           self.all_picture_data.append(data)
           self.montageDB.insert_new_picture(photo_location, face_encodings)
           return data
       else:
           return []

    def insert_batch_data_set_from_file(self, picture_file):
        for pic_file in os.listdir(picture_file):
            print("adding {}".format(pic_file))
            pic_abs_path = picture_file + pic_file
            self.add_picture(pic_abs_path)


    def get_all_photos_with_person_in(self, picture_file):
        list_of_photos_in = []
        person_encoding = encode_image(picture_file)
        if len(person_encoding)>0:
            #use first person identified in photo
            person_encoding = person_encoding[0]
            for pic in self.all_picture_data:
                pic_face_encodings_list = pic["face_encodings"]
                distance_of_person = is_in_photo(person_encoding, pic_face_encodings_list)
                if distance_of_person:
                    list_of_photos_in.append(pic["photo_location"])
            return list_of_photos_in
        else:
            return []

    def delete_all(self):
        self.montageDB.delete_all()

    def get_all(self):
        return  self.montageDB.get_all()




