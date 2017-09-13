import os

from pymongo import MongoClient

from tests.db_tests.test_data import TEST_DATA

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

    def delete_all_people(self):
        person_col = self.db.person
        person_col.remove({})

    def insert_test_data(self):
        person_col = self.db.person
        self.delete_all_people()
        test_data = TEST_DATA
        for per in test_data:
            self.insert_person(per)
        return person_col.find({}).count()

    def update_person(self, find_by, update):
        """
        :param find_by: dict e.g {name:"alex"}
        :param update: dict of field want to edit {"role":"DBA"}
        """
        person_col = self.db.person
        person_col.update(
            find_by,
            {'$set' : update}
        , upsert=False)

    def __del__(self):
        self.client.close()



if __name__ == "__main__":
    crud = Crud()
    crud.insert_test_data()
