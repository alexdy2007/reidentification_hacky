import face_recognition
from model.encode_image import encode_image
from db_connection.Crud import Crud

def compare_face_to_known(face_to_match, known_face_list, know_location, to_match_top=1):
    # Load a test image and get encondings for it
    encode_face_to_match = encode_image(face_to_match)
    encoded_known_faces = known_face_list[1]
    names_known_faces = known_face_list[0]
    if len(encode_face_to_match) == 0:
        return None
    # See how far apart the test image is from the known faces
    face_distances = face_recognition.face_distance(encoded_known_faces,
                                                    encode_face_to_match)

    person_distance_from_match = list(zip(names_known_faces, face_distances))
    person_distance_from_match.sort(key=lambda x: x[1])

    similar_people = person_distance_from_match[0:to_match_top]
    similar_people_records= []
    crud = Crud()

    for person in similar_people:
        if person[1] < 0.5:
            person = crud.get_person({"name":person[0]})[0]
            similar_people_records.append(person)
    return similar_people_records