from ex108 import currency

p = float(input('Enter the price: €'))
print(f'Half of {currency.coin(p)} is {currency.coin(currency.half(p))}.')
print(f'Double of {currency.coin(p)} is {currency.coin(currency.double(p))}.')
print(f'Increasing 10% of {currency.coin(p)} we have {currency.coin(currency.increase(p, 10))}.')
print(f'Decreasing 13% of {currency.coin(p)} we have {currency.coin(currency.decrease(p, 13))}.')
