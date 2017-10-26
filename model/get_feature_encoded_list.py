from db_connection.PeopleDB import PeopleDB

def get_feature_encoding_list():
    crud = PeopleDB()
    people = crud.get_person({"has_encodings":True})

    encoding_list = []
    name_list = []
    for person in people:
        name_list.append(person["name"])
        encoding_list.append(person["encoded_face"])

    return [name_list, encoding_list]

