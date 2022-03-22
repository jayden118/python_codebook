import json
from json import JSONEncoder

person = {"name": "John", "age": 21, "city": "San Francisco", "hasChildren": False, "titles": ["engineer, programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

#with open('person.json', 'w') as file:
#    json.dump(personJSON, file, indent=4) # dump without s is to store data to json file

person = json.loads(personJSON)
print(person)

#with open('person.json', 'r') as file:
#    person = json.load(file)
#    print(person, type(person))

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(obj):
    if isinstance(obj, User): # check obj is class of User
        return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')


user = User("Chin", 33)
print(user, type(user), user.name, user.age)

userJSON = json.dumps(user, default=encode_user)
print(userJSON, type(userJSON))


class UserEncoder(JSONEncoder): # encode object to dictionary
    def default(self, obj):
        if isinstance(obj, User):
            return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
        return JSONEncoder.default(self, obj)


userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON, type(userJSON))

userJSON = UserEncoder().encode(user)
print(userJSON)

def decode_user(dct): # decode dictionary to object
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct



user = json.loads(userJSON, object_hook=decode_user)
print(user.name, type(user))






