# __eq__ porownanie
# __lt__ mniejsza niż

class MyNumber:
    def __int__(self, value):
        self.value = value


class MyNumber2:
    def __int__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


#
# num1 = MyNumber(5)
# num2 = MyNumber(15)
# print(num1 < num2)


num3 = MyNumber2(5)

num4 = MyNumber2(15)
num5 =MyNumber2

print(num3 < num4)

print(num3==num4)
