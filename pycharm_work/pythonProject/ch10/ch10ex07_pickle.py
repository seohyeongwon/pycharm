import pickle

from pprint import pprint

person1 = {
    'name' : '홍길순',
    'height' : 170,
    'weight' : 60
}

person2 = {
    'name' : '홍길동',
    'height' : 200,
    'weight' : 80
}

people = [person1, person2]

with open("people.pickle", "wb") as f :
    pickle.dump(people, f)

with open("people.pickle", "rb") as f:
    loaded_people = pickle.load(f)

pprint(loaded_people)
