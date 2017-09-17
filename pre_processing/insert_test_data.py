from db_connection.Crud import Crud
import os
import random
from shutil import copyfile

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PICTURE_DIR = CURRENT_DIR + os.sep + ".." + os.sep + "webface" + os.sep + "src" + os.sep + "assets" + os.sep + "pictures" + os.sep
DATA_DIR = CURRENT_DIR + os.sep + ".." + os.sep + "data" + os.sep

ROLES = ["BI", "Dev", "Tester", "Discovery", "Product Owner", "Director", "Lab Manager"]


def insert_test_faces_into_db():

    crud = Crud()
    crud.delete_all_people()
    for person in os.listdir(DATA_DIR):

        person_dir = DATA_DIR  + person + os.sep
        for pic in os.listdir(person_dir):
            if "0001.jpg" in pic:
                name = " ".join(person.split("_"))
                role = ROLES[random.randint(0,6)]

                person_data_pic = DATA_DIR + person + os.sep + pic

                person_target_dir = PICTURE_DIR + person
                person_target_pic = person_target_dir + os.sep + person + ".jpg"

                if not os.path.exists(person_target_dir):
                    os.makedirs(person_target_dir)

                copyfile(person_data_pic, person_target_pic)
                person_data = {
                    "name":name,
                    "role":role,
                    "photo_location" : PICTURE_DIR + person + os.sep + person + ".jpg",
                    "has_encodings" : False
                }
                crud.insert_person(person_data)


insert_test_faces_into_db()
