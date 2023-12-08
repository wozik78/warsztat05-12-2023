#hermetyzacja enkapsulacja

class Boat:
    """
    dokumentacja klasy

    """
    def __init__(self,model,year):
        self.model=model
        self.year=year
        self.speed=0

    def sail(self):
        self.speed +=10

    def speedometer(self):
        print(f"speed in knots {self.speed}")

    def break_(self):
        self.speed -=10



b1 = Boat("Omega",2023)

b1.sail()
b1.sail()
b1.sail()
b1.sail()
b1.sail()

print(b1.speed)
b1.speedometer()






