from db_connection.Crud import Crud
from model.encode_image import encode_image

def encode_all_people_in_db():
    crud = Crud()
    people = crud.get_person({})
    for person in people:
        image_location = person["photo_location"]
        image_encoding = encode_image(image_location)
        if len(image_encoding)>0:
            crud.update_person(person, {"encoded_face":list(image_encoding), "has_encodings":True})


if __name__ == "__main__":
    encode_all_people_in_db()