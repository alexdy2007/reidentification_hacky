import os

CURRENT_DIR =  os.path.dirname(os.path.realpath(__file__))
PICTURE_DIR = "{0}{1}..{1}data{1}lfw_funneled".format(CURRENT_DIR, os.sep)


def get_faces(starts_with=None):
    people = {}
    for dirpath, dirnames, filenames in os.walk(PICTURE_DIR):
        if ".jpg" in filenames[0]:
            k = dirpath.split(os.sep)[-1]
            if k in people:
                people[k] = people[k] + filenames
            else:
                people[k] = filenames
    if starts_with is not None:
        people = {k:v for k,v in people.items() if k.startswith(starts_with)}
    return people



if __name__ == "__main__":
    people = get_faces("F")
    print("here")