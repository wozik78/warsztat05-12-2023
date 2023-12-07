#dekorator @dekorator_nazwa
#jako argument przjmuje inna funkcję
#dodanie nowej funkcjonalnosci do funkcji
#wykorzystuje zasadę funkcji wewnętrznej

def dekor(funk):
    def wew():
        print('dekorujemy')
        return funk()

    return wew
@dekor
def hej():
    print('hej')


hej()

#robimy dekorator


