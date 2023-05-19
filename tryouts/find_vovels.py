from dataclasses import dataclass
from typing import Callable


vovels_eng = ['a', 'e', 'i', 'o', 'u']

def find_vovels(string: str) -> int:
    result = 0
    for char in string.lower():
        if char in vovels_eng:
            result += 1
    
    return result


@dataclass
class TestCase:
    input: str
    expected: int


test_cases = [
    TestCase('Anna', 2),
    TestCase('why', 0),
]

def test(method: Callable):
    for test_case in test_cases:
        actual = method(test_case.input)
        assert actual == test_case.expected, f"{test_case.input}: {actual} != {test_case.expected}"

test(find_vovels)