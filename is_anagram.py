
from collections import defaultdict
from dataclasses import dataclass
from typing import Callable, Dict


def is_anagram(first: str, second: str) -> bool:     
    first_char_dict = _get_char_count_dict(first.lower())
    second_char_dict = _get_char_count_dict(second.lower())
    return first_char_dict == second_char_dict


def _get_char_count_dict(string: str) -> Dict[str, int]:
    result = defaultdict(int)
    for char in string:
        if char.isalnum():
            result[char] += 1
    return result


@dataclass
class TestCase:
    input: Dict
    expected: bool


test_cases = [
    TestCase({'first': 'a', 'second': 'b'}, False),
    TestCase({'first': 'qwe', 'second': '1'}, False),
    TestCase({'first': 'qwe', 'second': 'ewq'}, True),
    TestCase({'first': 'qwe', 'second': 'ewq--'}, True),
    TestCase({'first': 'aab', 'second': 'abb'}, False),
]

def test(method: Callable):
    for test_case in test_cases:
        actual = method(**test_case.input)
        assert actual == test_case.expected, f"{test_case.input}: {actual} != {test_case.expected}"

test(is_anagram)
