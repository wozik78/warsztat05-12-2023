import pickle
from dataclasses import dataclass
from person_kl10 import Person

#
# @dataclass
# class Person:
#     first_name:str
#     last_name:str
#     id:int



with open('dane.pickle','rb') as file:
    p=pickle.load(file)

print("--------------")

print(p)

for person in p:
    print(f"id{id}")

