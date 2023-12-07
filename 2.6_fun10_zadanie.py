# napisać funkcję która przyjmie age, first, last
# z tych parametrów zbuduje słownik
# age może być opcjonalne
# za pomocą pętli while ma pobrać dane od user i wywołać z parametrami tą funkcję
# zastosować klawisz ucieczki


def zwroc_slownik(first, last, age=None):
    person = {'first': first, 'name': last}
    if age:
        person['age'] = age

    return person


print(zwroc_slownik("radek", 'kowalski'))


while True:
    print("podaj imie i nazwisko:")

    print ("wpisz q aby zakończyć")

    f_name=input("Imie")
    if f_name=='q':
        break
    l_name = input("Imie")
    if l_name=='q':
        break
    age = input("wiek")
    if age =='q':
        break
    print(build_dict(f_name,l_name,age))