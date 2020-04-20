def increase(price=0, percent=0):
    result = price + (price * percent / 100)
    return result


def decrease(price=0, percent=0):
    result = price - (price * percent / 100)
    return result


def half(price=0):
    result = price / 2
    return result


def double(price=0):
    result = price * 2
    return result


def coin(price=0, coin='€'):
    return f'{coin}{price:.2f}'

