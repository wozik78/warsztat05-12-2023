# generatory --zwracają wynik operacji , mają wskaźnik który ustawiają na następny po każdej operacji
# odczyt sekwencyjny

def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # zwraca wynik i zapoamietuje , ustawia wskaźnik na nasepny

kwa=kwadrat2(5)
print(next(kwa))
print(next(kwa))
print(next(kwa))
try:
    print(next(kwa))
except StopIteration:
    print("zakończyłem działanie`")
