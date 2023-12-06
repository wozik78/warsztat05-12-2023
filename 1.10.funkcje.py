# funkcje --wydzielony fragment kodu który możena wykonać w dowolny momencie
# funkcja musi być najpierw zadekalrowana
# dopiero po zadeklarowaniu może być uzyta

a = 9
b = 8


def dodaj():
    print(a + b)



def dodaj2(a,b):
    print(a+b)

def odejmij(a,b,c=0):
    print(a-b-c)


dodaj2(2,4)
odejmij(1,2,0)


def mnozenie(a,b,c):
    return a*b*c

print(mnozenie(b=1,a=2,c=3))


def mnozenie2(a,)
