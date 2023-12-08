#autor
#tytuł
#isdn
class Book:

    def __int__(self,title,author, isbn):
        self.title=title
        self.author=author
        self.isbn=isbn

    def __repr__(self):
        return f"Author:{self.author}, Tytuł: {self.title}, ISBN: {self.isbn}"
#lista ksiazek do wypozyczenia
#lista ksiazek wypozyczonych
#dodanie ksiazki do biblioteki
#wypozycenie ksiazkki
#zwroc ksiazke
#znajdz ksiazke
class Library:

    def __int__(self):
        self.dostepne_ksiazki=[]
        self.wypozyczone_ksiazki =[]

    def fun_dodaj_ksiazke(self,book):
        self.dostepne_ksiazki.append(book)

    def fun_ksiazki_do_wypozyczenia(self):
        return self.dostepne_ksiazki

    def fun_ksiazki_wypozyczone(self):
        return self.wypozyczone_ksiazki

    def fun_wypozycz_ksiazke(self,isbn):
        #usunac z dostepnych
      for book in self.dostepne_ksiazki:
          if book.isbn ==isbn:
              self.dostepne_ksiazki.remove(book)
              self.wypozyczone_ksiazki.append(book)
          return book
       return Exception("Nie ma takiej Ksiazki")
        #dodac do wypozycoznych

     def fun_zwroc_ksiazke(self,isbn):
         for book in self.wypozyczone_ksiazki:
              if book.isbn == isbn:






