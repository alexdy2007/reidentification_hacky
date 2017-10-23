from db_connection import Crud

class MontageDB(Crud):

    def __init__(self):
        super().__init__()
        self.target_db = self.db.montagephotos

    def insert_new_picture(self, photo_location, face_encodings):
        """
        :param photo_location: path
        :param face_encodings: [[face encodings],[face encodings],...]
        """

        if len(face_encodings) > 0:
            data = {"photo_location":photo_location,
                    "face_encodings" : face_encodings}
            self.target_db.insert(data)

    def get_all(self):
        return self.target_db.find({})


    def delete_all(self):
        self.target_db.remove({})

