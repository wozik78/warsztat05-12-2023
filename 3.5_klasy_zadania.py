#stworzenie ksiazki telefonicznej z wykorzystaniem while
#dodaj kontak
#usun kontak
#wyszukaj
#wyswietl liste

#stworzyc system zarzadzania bibliateka
#dodaj skiaze ,usun ksiazke , wypozycz ksiazke ,zwroc ksiazke
#uzyc klass np book, library
#obsłuzyc blad
#moza dodac kalse user --bedzie pamietał jakies ksiazki wypozyczenie



class KsiazkaTelefoniczna:
            """
            klasa ksiazki telefonicznej

            """
    k_tel={}
    def __init__(self,nazwa,nr_tel):
         """
         Metoda inicjalizujaca

         :param self:
         :param a:
         """

         self.nazwa=nazwa
         self.nr_tel=nr_tel

    def __repr__(self):
        return f"{self.nazwa}{self.nr_tel}"


    def dodaj_kontakt(self):
        k_tel[self.nazwa]=self.nr_tel
        print("kontakt_dodany")

    def usun_kontakt(self):
        del k_tel[self.nazwa]
        print("kontakt_usuniety")

    def wyszukaj_kontakt(self):



    def wyswietl_liste(self):
        pass


