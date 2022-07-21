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


print(fibonacci(10))
print(fibonacci_short(10))
print(fibonacci_recursion(10))
