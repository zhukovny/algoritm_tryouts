'''
Дано целое число n. Требуется вывести все правильные скобочные последовательности длины 2*n, 
упорядоченные лексикографически 
'''

def func(n):
    generate('', 0, 0, n)


def generate(current, open, closed, n):
    if len(current) == 2 * n:
        print(current)
        return

    if open < n:
        generate(current + '(', open + 1, closed, n)

    if closed < open:
        generate(current + ')', open, closed + 1, n)

    
func(3)


# assert func(1) == [
#     '()',
# ]
# assert func(2) == [
#     '(())',
#     '()()',
# ]
# assert func(3) == [
#     '((()))',
#     '(()())',
#     '(())()',
#     '()(())',
#     '()()()',
# ]
