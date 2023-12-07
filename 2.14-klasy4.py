#missing -metoda wykonywana gdy nie ma klucza w słownik

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"

d_python = {}

d_python['name'] ='Radek'
print(d_python['name'])
#print(d_python['imie'])

d1= DefaultDict()

d1['name']='Radek'

print(d1['name'])
print(d1['imie'])


