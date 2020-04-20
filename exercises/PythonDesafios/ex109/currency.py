def increase(price=0, percent=0, form=True):
    result = price + (price * percent / 100)
    return result if form is False else coin(result)


def decrease(price=0, percent=0, form=True):
    result = price - (price * percent / 100)
    return result if form is False else coin(result)


def half(price=0, form=True):
    result = price / 2
    return result if form is False else coin(result)


def double(price=0, form=True):
    result = price * 2
    return result if form is False else coin(result)


def coin(price=0, coin='€'):
    return f'{coin}{price:.2f}'
