'''
Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.
'''

def func(elements):
    current = 0
    best = 0
    for e in elements:
        if e == '1':
            current += 1
            best = max(best, current)
        else:
            current = 0

    return best


assert func('') == 0
assert func('0') == 0
assert func('0011101') == 3
assert func('101101111') == 4
