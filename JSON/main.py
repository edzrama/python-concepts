import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# Serialization
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

with open("new_person.json", "w") as file:
    json.dump(person, file, indent=4)

# Deserialization
person = json.loads(personJSON)
print(person)

with open("new_person.json", "r") as file:
    person = json.load(file)
    print(person)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('John', 20)


def encode_user(obj):
    if isinstance(obj, User):
        return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError('Object type of User is not JSON Serializable')


userJSON = json.dumps(user, default=encode_user)
# type str
print(userJSON)

from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
        return JSONEncoder.default(self, obj)


# userJSON = json.dumps(user, cls=UserEncoder)
userJSON = UserEncoder().encode(user)
# type str
print(userJSON)

user = json.loads(userJSON)
# type dict
print(user)


def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(userJSON, object_hook=decode_user)
# type class User
print(type(user))
