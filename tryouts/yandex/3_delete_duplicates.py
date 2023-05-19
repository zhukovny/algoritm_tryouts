'''
Дан упорядоченный по неубыванию массив целых 32-разрядных чисел. 
Требуется удалить из него все повторения.
'''

def func(nums):
    if not nums:
        return []

    result = []
    last_num = nums[0]
    for n in nums:
        if last_num != n:
            result.append(last_num)
            last_num = n

    return result + [last_num]


assert func([]) == []
assert func([2, 4, 8, 8, 8]) == [2, 4, 8]
assert func([2, 2, 2, 8, 8]) == [2, 8]
assert func([2, 2, 2, 8]) == [2, 8]
