
# Нужно убрать из этой строки повторы и отсортировать по количеству повторяющихся слов

names = ['header', 'menu', 'menu-item', 'menu-item', 'menu-item', 'footer', 'menu', 'link', 'link', 'link', 'link']

def solution(input: list) -> list:
    names_dict = dict()
    for name in input:
        names_dict[name] = names_dict.get(name, 0) + 1
    
    return [key for key in sorted(names_dict, key=names_dict.get, reverse=True)]


print(solution(names))
