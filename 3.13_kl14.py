class MyError(Exception):
    def __int__(self, message, err_code):
        super().__init__(message)
        self.err_code = err_code


class MyValueError(MyError):
    def __int__(self, message):
        super().__int__(message, err_code=100)


class MyTypeError(MyError):
    def __int__(self, message):
        super().__int__(message, err_code=200)


def my_function(x: int, y):
    if not isinstance(x, int):
        raise MyTypeError('x must be integer')
    if not isinstance(y, int):
        raise MyTypeError('y must be integer')
    if y == 0:
        raise MyValueError("y cannot be zero")

    return x / y


try:
    result = my_function(4, 5)
except MyTypeError as e:
    print("złapałem błąd typu", e)
    print("kod błedu", e.err_code)
except MyValueError as e:
    print("złapałem błąd wartosci", e)
    print("kod błedu", e.err_code)
except Exception as e:
    print("blad", e)
else:
    print(f"dziala {result}")
finally:
    print("done")
