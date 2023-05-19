'''
Даны две строки, состоящие из строчных латинских букв. 
Требуется определить, являются ли эти строки анаграммами, 
т. е. отличаются ли они только порядком следования символов.
'''


from collections import defaultdict


def func(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False

    return chars_count_dict(first) == chars_count_dict(second)

def chars_count_dict(string: str) -> dict:
    result = defaultdict(int)
    for s in string:
        result[s] += 1
    return result
    

assert func('', 'a') is False
assert func('qwe', 'a') is False
assert func('qwe', 'qwe') is True
assert func('qweewq', 'qweqwe') is True
