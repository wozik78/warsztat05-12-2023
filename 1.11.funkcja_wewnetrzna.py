# funkcja wewnetrzna
# zasadę działania funkcji wewnetrznej w pythonie wykorzystuja dekoratory

# @dekorator

def fun1(c):
    print(f"to jest funkcja fun1{c}")

    def fwew(a, b):
        return  a * b
    return fwew # zwracamy aders funkcji

xFun = fun1()

print(xFun(2,3))