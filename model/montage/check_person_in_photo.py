import face_recognition

def is_in_photo(encoded_face, encoded_faces_in_photo):
    face_distances = face_recognition.face_distance(encoded_faces_in_photo,
                                                    encoded_face)
    for idx, distance in enumerate(face_distances):
        if distance<0.45:
            return distance
    return None

