# Задача: создать фукцию или объект, суммирующий числа, который можно было бы вызывать в виде
# chain_sum(5)(2)() = 7


def chain_sum_1(number):
    def wrapper(number2=None):
        if not number2:
            return wrapper.result
        wrapper.result += number2
        return wrapper
    wrapper.result = number

    return wrapper


def chain_sum_2(number):
    def wrapper(number2=None):
        try:
            wrapper.result += number2
        except TypeError:
            return wrapper.result
        return wrapper
    wrapper.result = number
    return wrapper


def chain_sum_3(number):
    def wrapper(number2=None):
        def inner():
            wrapper.result += number2
            return wrapper

        logic = {
            type(None): lambda: wrapper.result,
            int: inner
        }
        return logic[type(number2)]()


    wrapper.result = number
    return wrapper


class chain_sum_4:
    def __init__(self, number: int):
        self._number = number

    def __call__(self, value: int = 0):
        return chain_sum_4(self._number + value)

    def __str__(self) -> str:
        return str(self._number)


class chain_sum_5(int):
    def __call__(self, value: int = 0):
        return chain_sum_5(self + value)


print(chain_sum_1(5)(2)())
print(chain_sum_2(5)(2)()) 
print(chain_sum_3(5)(2)())
print(chain_sum_4(5)(2))
print(1 + chain_sum_5(5)(2))
