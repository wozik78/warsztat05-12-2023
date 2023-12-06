for i in range(10):
    print(i)

for i in range(1, 10):  # 1,9
    print(i)

for i in range(10):
    for j in range(10):
        print(i, j)

lista2 = [j for j in range(10)]
print(lista2)

for c in lista2:
    print(c)

# if-warunek

if True:
    pass  # nic nie robi
a = 1

if a == 1:
    print(f"A rowna się 1")
else:
    print("A nie równa sie 1")

a = 20

if a == 1:
    print("1")
elif a == 20:
    print("20")
else:
    print("coś tam")

for c in lista2:
    if c % 2 == 0:
        print(c, "parzysta")

lista4 = [j for j in range(10) if j % 2 == 0]
print(lista4)


#while  pętla sterowana warunkiem

licznik=0
while licznik<10:
    licznik+=1
    print("komunikat")


lista =[]

lista2 = []

while True:
    print("dzialam")
    wej = input("podaj liczbe") # str
    if not wej.isnumeric():
        break
    lista2.append(int(wej))

print(lista2)





