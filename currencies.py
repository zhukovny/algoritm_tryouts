input = [
    ['usd', 'buy', 10000],
    ['usd', 'sell', 5000],
    ['gbp', 'buy', 9000],
    ['eur', 'sell', 7000],
    ['uah', 'buy', 10000],
    ['usd', 'sell', 25000],
]


output = {
    # 'currency': [sum_buy, sum_sell]
    'usd': [10000, 30000],
    'gbp': [9000, 0],
    'eur': [0, 7000],
    'uah': [10000, 0]
}


def func(input):
    result = {}
    for currency, operation, value in input:
        sums = result.get(currency, [0, 0])
        sums[0 if operation == 'buy' else 1] += value        
        result[currency] = sums

    return result


result = func(input)
assert result == output
