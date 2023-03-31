from dataclasses import dataclass


maze = [
  [1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 0, 1],
  [0, 0, 0, 0, 0, 0],
  [0, 1, 1, 1, 1, 1],
  [0, 0, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 0]
]

# нули - путь, единицы - стены
# понять, есть ли выход из лабиринта, при условии что мы знаем где должен быть старт и финиш


@dataclass
class Coord:
    x: int
    y: int


def func(data: list, finish_coord: list) -> bool:
    last_path_coords = []
    for y in range(len(data)):
        current_path_coords = []
        row = data[y]
        for x in range(len(row)):
            cell = row[x]
            if cell == 0:   # path 
                current_path_coords.append(Coord(x, y))             
                if x in {coord.x for coord in last_path_coords}: 
                    break
           
        last_path_coords = current_path_coords
    return last_path_coords[-1] == finish_coord

finish = Coord(5, 5)
assert func(maze, finish) == True
            
        




