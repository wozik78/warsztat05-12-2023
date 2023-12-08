
contact ={}

while True:
    print(f"""
            1. Dodaj komentarz
            2.Usun komentarz
            3.wyszukaj kontakt
            4.wyswietl liste kontaktow
            5.koniec
            """)

    odp =input("co chcesz zrobić")

    if odp== '1':
        name=input("podaj imie")
        number=input("numer_telefonu")
        if not number.isdigit():
            raise ValueError ("numer_telefonu powinien zawierac cyfry")
        else:
            contact[name.lower()]=number
    elif odp=='2':

        name = input("podaj nazwę kontaktu")
        del contact[name]

    elif odp=='3':
        pass
    elif odp=='4':
        pass
    else:
        break
print("zakonczenie dzialania programu")