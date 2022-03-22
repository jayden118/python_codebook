# Error and Exceptions

try:
    a = 5 / 0
except Exception as error:
    print(error)


try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as error:
    print(error)
except TypeError as error:
    print(error)
else:
    print("Everything is fine!")
finally:
    print("Done!")


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooSmallError("Value is too small", x)


try:
    test_value(3)
except ValueTooHighError as error:
    print(error)
except ValueTooSmallError as error:
    print(error.message, error.value)