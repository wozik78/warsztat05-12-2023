# lambda skrócony zapis funkcji
# możliwość deklaracji w miejscu

def liczymy(x, y):
    return (x * y)


print(liczymy(5, 6))

liczymy2 = lambda x, y: x * y

print(liczymy2(7, 6))

lista = [1, 2, 3, 4, 5, 6, 7, 20, 55, 100, 123]

lista2 = []

for i in lista:
    lista2.append(i * 2)
print(lista2)

print([i * 2 for i in lista])

# map() wez wszystkie wartosci w kolekcji i wykonaj zananie

print(f"uzycie map(){list(map(lambda x: x * 2, lista))}")

print(f"uzycie filnetr(){list(filter(lambda x: x > 8, lista))}")

# reduce()


liczby = [1, 2, 3, 4, 5]

print(reduce(lambda a, b: a + b, liczby))
