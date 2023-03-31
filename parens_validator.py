from collections import defaultdict


parens_dict = {
    '(': ')',
    '{': '}',
    '[': ']',
}


def func(input_str: str) -> bool:
    if len(input_str) % 2 != 0:
        return False
    
    stack = []
    for char in input_str:
        if char in parens_dict.keys():
            stack.append(char)
        else:
            if stack == []:
                return False
            
            open_bracket = stack.pop()
            if char != parens_dict[open_bracket]:
                return False
            
    return stack == []
    
    



assert func('(') is False
assert func(')()') is False
assert func('()') is True
assert func('()()') is True
assert func('())') is False
assert func('(())') is True
assert func('[()]') is True
assert func('[(])') is False
