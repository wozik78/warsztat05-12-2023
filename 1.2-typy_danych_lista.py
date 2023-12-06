# kolekcja przechowująca dowolną ilość dowolnych danych na raz
# zaletą listy jest zachowanie kolejności przy dodawaniu
# oznacza to że jak dodajemy elementy to zostaną one dodane na końcu listy

lista = []

print(lista)

lista.append("radek")
lista.append("zenek")
lista.append("dupa")
print(lista)
print(lista[-1])
print(len(lista))

print(lista[0:3])

print(lista[-1::-1])

lista[0] = 'Piotr'
print(lista)
lista.insert(1, "Kamil")
print(lista)

#usuniecie

lista.remove("Piotr")

print(lista)

lista2=lista  # kopia referencji

lista_copy=lista.copy()

print(lista_copy)

lista_copy.clear()


print(lista)


lista3 ="definicja"

lista4 =[]

lista4.extend(lista3)

print(lista4) #rozpakowanie sekwencji

lista5=[lista3]
print(lista5)

krotka=tuple(lista5)

print(krotka)








