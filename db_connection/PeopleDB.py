from db_connection.Crud import Crud
import os

class PeopleDB(Crud):

    def __init__(self):
        super().__init__()
        self.target_db = self.db.person


    def get_person(self, query):
        persons_found = self.target_db.find(query)
        return list(persons_found)

    def insert_person(self, person):
        person_col = self.target_db
        if "name" in person:
            file_name = self.PICTURE_DIR + person["name"] + os.sep + person["name"]
            person_col.insert(person)
        else:
            return ValueError("No Name Provided")

    def delete_all_people(self):
        self.target_db.remove({})

    def insert_test_data(self, test_data=None):
        person_col = self.db.person
        self.delete_all_people()
        for per in test_data:
            self.insert_person(per)
        return person_col.find({}).count()

    def update_person(self, find_by, update):
        """
        :param find_by: dict e.g {name:"alex"}
        :param update: dict of field want to edit {"role":"DBA"}
        """
        self.target_db.update(
            find_by,
            {'$set': update}
            , upsert=False)
