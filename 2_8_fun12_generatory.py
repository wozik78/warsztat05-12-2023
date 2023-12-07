generator_1 = [x for x in range[5]]
print(generator_1)
print(type(generator_1))


generator2 = (x for x in range(10))

def generator3()
    for x in [1,2,3,4,5]:
        yield x


g3= generator3()

print(next(g3))

print(next(g3))


def fibo():
    a,b=0,1
    while True:
        yield b
        a,b=b,a+b
fi=fibo()

print(next(fi))
print(next(fi))

print(next(fi))
print(next(fi))

print(next(fi))
print(next(fi))

def fibo_with_index(n):
    a,b=0,1


