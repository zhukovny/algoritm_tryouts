import json
from typing import Iterable
import unittest
from urllib.parse import urlparse


raw_data = '''{
    "example1": {
        "plain": {
            "url": "https://mail.ru"
        },
        "nested": {
            "url": "http://mail.ru"
        },
        "array": [
            {
                "url": "https://yandex.ru"
            },
            {
                "url": "https://google.com"
            },
            {
                "url": null
            },
            "ftp://192.168.1.1",
            "ws://192.168.1.2",
            "ws://"
        ],
        "url": "https://yahoo.com"
    },
    "example2": {
        "url": "https://finance.yahoo.com",
        "array": [
            {
                "url": "https://news.yandex.ru"
            }
        ],
        "nested_dict": {
            "level_one": {
                "url": "https://yahoo.com"
            },
            "level_two": {
                "list": [
                    "wss://192.168.1.4",
                    {
                        "url": "https://yandex.ru"
                    },
                    "https://google.com",
                    596
                ]
            }
        }
    },
    "url": "http://finance.yahoo.com/"
}'''


expected_result = [
    "http://finance.yahoo.com/",
    "http://mail.ru",
    "https://finance.yahoo.com",
    "https://google.com",
    "https://mail.ru",
    "https://news.yandex.ru",
    "https://yahoo.com",
    "https://yandex.ru",
    "ftp://192.168.1.1",
    "ws://192.168.1.2",
    "wss://192.168.1.4",
]


def is_url(value: str) -> bool:
    url = value.strip()
    if not url:
        return False
    
    result = urlparse(url)
    
    if not result.scheme or not result.netloc: 
        return False        
    
    return True


def find_in(data: Iterable) -> Iterable:
    result = []
    
    for value in data:
        if isinstance(value, str):
            if is_url(value):
                result.append(value)
                
        if isinstance(value, dict):
            result += find_in(value.values())
            
        if isinstance(value, list):
            result += find_in(value)            
                
    return result


def function(raw_data: bytes):
    """
    Тело функции для задачи
    """
    data = json.loads(raw_data)    
    return find_in(data.values())


class TestStringMethods(unittest.TestCase):
    def test_task(self):
        result = function(raw_data)
        print(result)
        self.assertEqual(set(result), set(expected_result))


if __name__ == '__main__':
    unittest.main()

