def fibonacci(n: int) -> int:
    nums = [0, 1]
    for _ in range(2, n + 1):
        nums.append(nums[-1] + nums[-2])

    return nums[n]


def fibonacci_short(n: int) -> int:    
    if n < 2:
        return n

    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b


def fibonacci_recursion(n: int) -> int:
    if n < 2:
        return n

    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


def nearest_fibonacci(n):
    a = b = 1
    # пока сумма A и B меньше квадрата входного числа
    while 2 * n > a + b:
        # в A кладем B, в B сумму A и B
        a, b = b, a + b
    return a


# print(fibonacci(10))
# print(fibonacci_short(10))
# print(fibonacci_recursion(10))
print(nearest_fibonacci(10))
