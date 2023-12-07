#dziedziczenie

class Contact:
    all_contact=[] #pusta lista

    def __int__(self,name,email):
        self.name=name
        self.email=email
        Contact.all_contact.append(self)
    def __repr__(self):
        return f'{self.name}{self.email}'



    class Suplier(Contact):



c1=Contact("Adam","admin@wp.pl")
c2=Contact("Adam1","admin1@wp.pl")
c3=Contact("Adam2","admin2@wp.pl")
print(c1.all_contact)

s= Suplier("Marek","dupa@whp.pl")
print(s)
print(c1.all_contact)