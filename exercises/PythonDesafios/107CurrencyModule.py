from ex107 import currency

p = float(input('Enter the price: € '))
print(f'Half of {p} is {currency.half(p)}.')
print(f'Double of {p} is {currency.double(p)}.')
print(f'Increasing 10% of {p} we have {currency.increase(p, 10)}.')
print(f'Decreasing 13% of {p} we have {currency.decrease(p, 13)}.')
