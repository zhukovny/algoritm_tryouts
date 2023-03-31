def find_intersection(a, b):
    
    result = []               
                
    for _a in a:
        a_range = list(range(_a[0], _a[1] + 1))
        for _b in b:
            b_range = list(range(_b[0], _b[1] + 1))
            intersection = sorted(list(set(a_range).intersection(b_range)))
            if intersection:
                result.append([intersection[0], intersection[-1]])
    
    return result


a = [[0, 2], [5, 10], [13, 23], [24, 25]]
b = [[1, 5], [8, 12], [15, 18], [20, 24]]

expected = [[1, 2], [5, 5], [8, 10], [15, 18], [20, 24]]
actual = find_intersection(a, b)

assert actual == expected, f'{actual} != {expected}'
