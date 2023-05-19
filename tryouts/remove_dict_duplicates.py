'''
Дано: список dict-объектов вида вида {'key': 'value'}, 
например [{'key1': 'value1'}, {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}, {}, {}, {'key1': 'value1'}, {'key1': 'value1'}, {'key2': 'value2'}].
Напишите функцию, которая удаляет дубликаты из этого списка. 
Для примера выше возвращаемое значение может быть равно [{'key1': 'value1'}, {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}, {}, {'key2': 'value2'}].
Обязательное условие: функция не должна иметь сложность O(n^2).
'''
from typing import Dict
from typing import List

input = [
    {'key1': 'value1'},
    {
        'k1': 'v1',
        'k2': 'v2',
        'k3': 'v3',
    },
    {},
    {},
    {'key1': 'value1'},
    {'key1': 'value1'}, 
    {'key2': 'value2'},
]


def func(dicts_list: List[Dict]) -> List[Dict]:
    hash_map = dict()
    for d in dicts_list:
        h = hash(tuple(sorted(d.items())))
        if h not in hash_map:
            hash_map[h] = d

    return list(hash_map.values())


expected = [
    {'key1': 'value1'},
    {
        'k1': 'v1',
        'k2': 'v2',
        'k3': 'v3',
    },
    {},
    {'key2': 'value2'},
]

assert func(input) == expected
