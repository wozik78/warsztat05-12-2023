import pickle
from dataclasses import dataclass


# class Person:
#     def __init__(self, fn,ln,id):
#         self.fn=fn
#         self.ln=ln
#         self.id=id
#
@dataclass
class Person:
    first_name: str
    last_name: str
    id: int


pq1 = Person("maciek", "nowak", 1)
print(pq1)
p2=Person("tomek","kowalski",2)
print(p2)

people=[pq1,p2]

print(people)
with open('dane.pickle','wb') as stream:
    pickle.dump(people,stream)