'''
Нужно реализовать join по первому элементу кортежа
'''

# l1 = [(k1, a1_1), (k1, a1_2), (k2, a2), (k3, a3)]
# l2 = [(k1, b1), (k3, b3), (k5, b5)]
#result_inner = [(k1, a1, b1), (k3, a3, b3)]

# select * from l1 join l2 on l1[0] = l2[0];
# k1, a1_1, b1
# k1, a1_2, b1
# k3, a3, b3

from collections import defaultdict


def func1(l1, l2):
    result = []
    for i in l1:
        for j in l2:
            if i[0] == j[0]:
                result.append((i[0], i[1], j[1]))

    return result




def func2(l1, l2):
    d2 = defaultdict(list)
    for key, value in l2:
        d2[key].append(value)

    result = []
    for key, value1 in l1:
        value2 = d2.get(key)
        for v in value2:
            result.append((key, value1, v))

    return result

