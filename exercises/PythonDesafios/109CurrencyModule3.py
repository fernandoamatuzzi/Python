from ex109 import currency

p = float(input('Enter the price: €'))
print(f'Half of {currency.coin(p)} is {currency.half(p, True)}.')
print(f'Double of {currency.coin(p)} is {currency.double(p, True)}.')
print(f'Increasing 10% of {currency.coin(p)} we have {currency.increase(p, 10, True)}.')
print(f'Decreasing 13% of {currency.coin(p)} we have {currency.decrease(p, 13, True)}.')
