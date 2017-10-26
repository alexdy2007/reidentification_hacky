from flask_restful import Resource
from db_connection.PeopleDB import PeopleDB
from flask import jsonify, request

crud = PeopleDB()

class Person(Resource):

    def get(self, role=None, name=None):
        query = {}
        if name:
            query["name"] = name
            query["role"] = role
        people = crud.get_person(query)
        for p in people:
            if "encoded_face" in p: del p["encoded_face"]
            del p["_id"]
        return jsonify(people)


    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return jsonify(data)
        elif "name" in data:
            crud.insert_person(data)

        return {"data":"Added"}
