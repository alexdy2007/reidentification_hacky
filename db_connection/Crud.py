from pymongo import MongoClient
import os
from db_connection.test_data import TEST_DATA
from pathlib import Path

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PICTURE_DIR = CURRENT_DIR + os.sep + ".." + os.sep + "pictures" + os.sep

class Crud(object):

    URI_CONNTECTION_STRING = "mongodb://localhost:27017/"

    def __init__(self):
        self.client = MongoClient(self.URI_CONNTECTION_STRING)
        self.db = self.client.facialrecdb

    def get_person(self, query):
        person_col = self.db.person
        persons_found = person_col.find(query)
        return list(persons_found)

    def insert_person(self, person):
        person_col = self.db.person
        if "name" in person:
            file_name = PICTURE_DIR + person["name"] + os.sep + person["name"]
            person_col.insert(person)
        else:
            return ValueError("No Name Provided")

    def insert_test_data(self):
        person_col = self.db.person
        person_col.remove({})
        test_data = TEST_DATA
        for per in test_data:
            self.insert_person(per)
        return person_col.find({}).count()

if __name__ == "__main__":
    crud = Crud()
    crud.insert_test_data()
