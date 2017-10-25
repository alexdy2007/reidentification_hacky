from unittest import TestCase
from db_connection.PeopleDB import PeopleDB

class TestDB(TestCase):
    def setUp(self):
        self.crud = PeopleDB()

    def test_insert_testdata(self):
        number_inserted = self.crud.insert_test_data()
        self.assertEqual(number_inserted, 5, "5 people should have been inserted")

    def test_find_alex(self):
        persons_found = self.crud.get_person({"name":"Alex Young"})
        self.assertEqual(persons_found[0]["name"], "Alex Young")

    def test_update(self):
        PoI = {"name":"Alex Young"}
        update = {"role" : "test"}
        update2 = {"role" : "test2"}
        self.crud.update_person(PoI, update)
        person = self.crud.get_person(PoI)
        self.assertEqual(person[0]["role"], "test")
        self.crud.update_person(PoI, update2)
        person = self.crud.get_person(PoI)
        self.assertEqual(person[0]["role"], "test2")

