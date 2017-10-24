from db_connection.Crud import Crud
import numpy as np
from bson.binary import Binary
import pickle

class MontageDB(Crud):

    def __init__(self):
        super().__init__()
        self.target_db = self.db.montagephotos

    def insert_new_picture(self, photo_location, face_encodings):
        """
        :param photo_location: path
        :param face_encodings: [[face encodings],[face encodings],...]
        """
        face_encodings_bin = Binary(pickle.dumps(face_encodings, pickle.HIGHEST_PROTOCOL))
        if len(face_encodings) > 0:
            data = {"photo_location":photo_location,
                    "face_encodings" : face_encodings_bin}
            self.target_db.insert(data)

    def get_all(self):
        data = [x for x in self.target_db.find({})]
        for d in data:
            d["face_encodings"] = pickle.loads(d["face_encodings"], )
        return data


    def delete_all(self):
        self.target_db.remove({})

