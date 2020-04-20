def increase(price, percent):
    result = price + (price * percent/100)
    return result


def decrease(price, percent):
    result = price - (price * percent/100)
    return result


def half(price):
    result = price / 2
    return result


def double(price):
    result = price * 2
    return result

