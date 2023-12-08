#wielodziedziczenie


class A:
    def method(self):
        print ("Metoda z klasy A")

class B:
    def method(self):
        print ("Metoda z klasy B")


class C(B,A):
    """
     Klasa dziedziczy po klasach

    """

class D(A,B):
    """
    Klasa d
    """


class E(A,B):
    """
    klasa D
    """


class F(B,A):
    """
    Klasa F
    """
class G(A,B):
    super().method()#wykonuje metode z klasy A
    print("Dopisane")

a=A()
a.method()


b= B()
b.method()


c=C()
c.method()


d=D()
d.method()

e=E()
e.method()
print(E.__mro__)
