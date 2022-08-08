from dataclasses import dataclass
from typing import Callable


def is_palindrome(phrase: str) -> bool:
    if len(phrase) < 2:
        return False

    phrase = "".join(phrase.split()).lower()
    reversed_phrase = "".join(reversed(phrase))
    return phrase == reversed_phrase


@dataclass
class TestCase:
    input: str
    expected: bool


test_cases = [
    TestCase('', False),
    TestCase('a', False),
    TestCase('racecar', True),
    TestCase('table', False),
    TestCase('Anna', True),
    TestCase('А роза упала на лапу азора', True),
    TestCase('123123', False),
]

def test(method: Callable):
    for test_case in test_cases:
        actual = method(test_case.input)
        assert actual == test_case.expected, f"{test_case.input}: {actual} != {test_case.expected}"

test(is_palindrome)
