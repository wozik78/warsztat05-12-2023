import pickle
from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

print("klasa person")