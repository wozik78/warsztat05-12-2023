# abstrakcja-----

from abc import  abstractmethod


class Counter:
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    def drukuj(self):
        pass

class Abc(Counter):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by
    @abstractmethod
    def drukuj(self):
        pass






class BoundedCounter(Counter):
    MAX = 100

    def __int__(self, values=0):
        if values > self.MAX:
            raise ValueError("wartość nie moze byc wieksza od Max")
        super().__init__(values)
    def drukuj(self):
        print("drukuje:",self.values)

class NewCounter(Counter):
    """
    licznik bez metoryd drukuj()
    """

##po oznaczneiu metody jako abstrakcyjnej


c = Counter()
c.increment()
c.drukuj()

bc = BoundedCounter()
bc.increment()
bc.drukuj()

nc=NewCounter()
