"""
У нас есть конфиг, который записан как json: 

{
    "service_version": "2022.08.02",
    "logs_store": {
        "remote": { 
            "url": "https://elk",
            "user": "some_user",
            "password": "some_password"
        }, 
        "local": "$HOME/service.log"
    },
    "message_broker": 
    {
        "url": "https://rabbitmq",
        "user": "rmq", 
        "password": "some_password"
    }
}

Необходимо написать функцию, которая приводит его к "плоскому" виду: 


{
    "service_version": "2022.08.02",
    "logs_store.remote.url": "https://elk",
    "logs_store.remote.user": "some_user",
    "logs_store.remote.password": "some_password",
    "logs_store.local": "$HOME/service.log",
    "message_broker.url": "https://rabbitmq",
    "message_broker.user": "rmq", 
    "message_broker.password": "some_password"
}
"""


def func(data: dict, parent_key: str = None) -> dict:
    result = dict()
    for key, value in data.items():
        new_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(value, str):
            result[new_key] = value
        else:
            result.update(func(value, new_key))
            
    return result


data = {
    "service_version": "2022.08.02",
    "logs_store": {
        "remote": { 
            "url": "https://elk",
            "user": "some_user",
            "password": "some_password"
        }, 
        "local": "$HOME/service.log"
    },
    "message_broker": 
    {
        "url": "https://rabbitmq",
        "user": "rmq", 
        "password": "some_password"
    }
}

expected = {
    "service_version": "2022.08.02",
    "logs_store.remote.url": "https://elk",
    "logs_store.remote.user": "some_user",
    "logs_store.remote.password": "some_password",
    "logs_store.local": "$HOME/service.log",
    "message_broker.url": "https://rabbitmq",
    "message_broker.user": "rmq", 
    "message_broker.password": "some_password"
}


actual = func(data)
assert actual == expected
