# krotka -kolekcja niezmienna(immutable)
# wie ile mu potrzeba pamięci i jest wydajniejsza
# krotka może być jednoelementowa

tupla1 = "radek",
print(type(tupla1))

tupla2 = 'radek', 'maciek', 'michał', 'gosia'

print(type(tupla2))

print(tupla2.index("radek"))

# rozpakowanie tupli

#a, b = 1, 2

#print(type(1, 2))


#a,*b=1,2,3,4,5 #* to taki worek na pozostałe zmienne

#print(a)
#print(b)

tupla4 = 'radek', 'maciek', 'michał', 'gosia'
a,b,*c =tupla4

print(a)
print(b)
print(c)



lista_krotka=list(tupla4)
print(lista_krotka) #