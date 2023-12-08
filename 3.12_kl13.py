#Exception
#tworzyć wyjątki nadpisujac klase  Exception
#class

class MyException(Exception):
    def __int__(self,message):
        super().__init__(message)

try:
    x=int(input("podaj liczbę całkowita"))
    if x<0:
        raise MyException("liczba musi byc dodatnia")
except MyException as e:
    print("wystapił wyjatek my exception")
except ValueError:
    print("wystapil blad wartosci")
except TypeError:
    print("blad typu")
except Exception as e:
    print("blad",e)
else:
    print(f"wprowadziles poprawne wartosci {x}")
finally:
    print("dane zostay wprowadzone")