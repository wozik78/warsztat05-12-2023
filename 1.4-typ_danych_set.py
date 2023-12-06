# set -zbiór brak duplikatów przechowuje unikalne wartosci nie zachowuje koleności przy dodawaniu elementow

lista = [33, 12, 34, 56, 78, 98, 33]

zbior = set(lista)
print(zbior)

zbior.add(18)
zbior.add(33)

print(zbior)

print(zbior.remove(33))

print(zbior)
print(zbior.pop())

print(sorted(zbior))


zb2 = set()

print(type(zb2))

print(zbior|zb2)##suma zbiorow

print(zbior&zb2) ##czesc wspolna

print(zbior.difference(zb2))

zbior.update(zb2)

print(zb2)




