print("nazywam się Maciek")
# pep8 --zasady pisania czystego kodu w pythonie
print('Nazwyam się Maciek2')
print(39)
print(type(39))
print("933")
print("933" + "mama")  # konkatenacja
# ctrl alt l pep8 poprawa
print("ala" * 3)
print(14 + 78)
# zmienna
name = 39
# pudełko do którego wrzucasz dane
# musi mieć nazwę
# typowanie dynamiczne tzn typ jest wnioskowany na podstawie tego co wrzucimy
# snake_case

print(name)
print(type(name))  # class int ---nazwa zmiennej powinna nam mówić o tym co przechowuje

# print("45" + 15)  # to sie nie uda
# szybki komentarz ctrl slash

print(int("45") + 15)  # a to już tak

wiek = 47
rok = 2023

temp = 36.6  # float

print(0.1 + 0.5)

print(0.1 + 0.7)  # to nie jest bład tylko ficzer

print(0.1 + 0.2)  # to też

# przy float wystepuje bład zaokraglenia

# typ decimal do obliczeń bez błędu zaokrąglenia

print(wiek + rok)
print(wiek - rok)
print(wiek / rok)  # wynikiem dzielenia jest float
print(wiek // rok)  # bez reszty
print(wiek ** rok)

print(len(str(wiek ** rok)))

print(54 - 5 * 43 + 4 / 2 + 4 / 2)

wersja = 3.900001
print(f"uzywamy wersji pythona{wersja}")  # f-string formatowanie
print("uzywamy {}".format(wersja))
print("uzywamy %f" % wersja)

print("""
tekst wielolinijkowy

""")

imie = "Maciek Maciek"

# imie.upper()   #ctrl i klik na funkcji odsyła do dokumentacji

tekst = imie.upper()

print(tekst)

liczba = 456789806064565

print(liczba)

print(f"nasz liczba {liczba:,}".replace(",", "."))

# typ logiczny


##tubnine to jest ai do programowania w pythonie


##Mateusz mazurek blog

##w3wschool

##hackerrank


# typ logiczny

# True False

# prawda fałsz


czy_znasz_python = True

print(czy_znasz_python)

print(type(czy_znasz_python))

print(int(True))
print(int(False))
print(bool("radek"))
print(bool(0))
print(bool(""))
print(bool(None))

tekst = '    tekst    '
print(tekst.strip())
print(tekst.lstrip())

tekst_x='Witaj świecie'
encode_s=tekst_x.encode('utf-8')
print(encode_s)
print(encode_s.decode('utf-8'))
#alt shift e odpali tylko kawałek kodu








