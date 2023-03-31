def qsort(array: list) -> list:
    if len(array) < 2:
        return array

    # этот алгоритм работает в среднем быстрее, если опорный элемент брать из середины
    ref_num = array[int(len(array) / 2)] 
    less = []
    more = []
    for num in array:
        if num < ref_num:
            less.append(num)
        if num > ref_num:
            more.append(num)

    return qsort(less) + [ref_num] + qsort(more)


l = [3, 5, 8, 1, 7]

print(qsort(l))
