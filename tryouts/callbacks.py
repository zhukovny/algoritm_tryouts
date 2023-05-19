from typing import Callable
from typing import List


# этот код содержит ошибку
def create_handlers(callback: Callable) -> List[Callable]:
    handlers_list = []
    for step in range(5):
        # ошибка тут. При вызове callback в него всегда попадает последнее значение step
        handlers_list.append(lambda: callback(step))
    return handlers_list


def execute_handlers(handlers: List[Callable]):
    for handler in handlers:
        handler()


execute_handlers(create_handlers(print))


# переписал вот так
def create_handler_parameters() -> List[int]:
    return [i for i in range(5)]


def execute_handler_with_parameters(handler: Callable, params: List[int]):
    for param in params:
        handler(param)


execute_handler_with_parameters(print, create_handler_parameters())
