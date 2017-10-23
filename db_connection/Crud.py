import os

from pymongo import MongoClient

from tests.db_tests.test_data import TEST_DATA
from datetime import datetime, timedelta


#mongo -u ian -p secretPassword 123.45.67.89/cool_db

class Crud(object):

    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    PICTURE_DIR = CURRENT_DIR + os.sep + ".." + os.sep + "pictures" + os.sep

    def __init__(self, remote=False):
        if remote:
            self.URI_CONNTECTION_STRING = "mongodb://localhost:27017/"
        else:
            self.URI_CONNTECTION_STRING = "mongodb://localhost:27017/"

        self.client = MongoClient(self.URI_CONNTECTION_STRING)
        self.db = self.client.facialrecdb



    def person_seen_db_insert(self, person):
        new_person = {}
        person_seen_db = self.db.personSeen
        new_person["name"] = person["name"]
        new_person["time_seen"] = datetime.now()
        if "encoded_face" in person:
            del person["encoded_face"]
        person_seen_db.insert(new_person)


    def find_someone_seen_in_last_x_seconds(self, seconds):
        person_seen_db = self.db.personSeen
        dt_x_second_ago  = datetime.now() - timedelta(seconds=seconds)
        query =  {"time_seen":{'$gt':dt_x_second_ago}}
        limit_to_fields = {"name":1}
        people_seen = person_seen_db.find(query, limit_to_fields).distinct("name")
        return people_seen


    def __del__(self):
        self.client.close()



if __name__ == "__main__":
    crud = Crud()
    crud.insert_test_data()
