islands_count = 0


data = [
    [1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
]


def func(data):
    islands_count = 0
    islands_indexes = []
    for y in range(len(data)):
        row = data[y]
        island_size = 0
        island_indexes = []
        for x in range(len(row)):
            value = row[x]
            if value == 1:
                island_size += 1
                island_indexes.append(x)
            if value == 0 and island_size > 0:
                islands_count += 1
                island_size = 0
            
    return islands_count

print(func(data))
        

        
