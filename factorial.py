def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

def factorial_recursion(n):
    return n * factorial_recursion(n - 1) if n != 0 else 1

print(factorial_recursion(5))
