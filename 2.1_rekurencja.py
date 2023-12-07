# rekurencja
# funkcja, która wywołuje samą siebie


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


print(silnia(5))


def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)
