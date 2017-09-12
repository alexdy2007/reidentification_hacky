from unittest import TestCase
from db_connection.Crud import Crud

class TestDB(TestCase):
    def setUp(self):
        self.crud = Crud()

    def test_insert_testdata(self):
        number_inserted = self.crud.insert_test_data()
        self.assertEqual(number_inserted, 5, "5 people should have been inserted")

    def test_find_alex(self):
        persons_found = self.crud.get_person({"name":"Alex"})
        self.assertEqual(persons_found[0]["name"], "Alex")