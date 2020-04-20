print('-' * 30)
print('{:^30}' .format('GOOD PLACE STORE'))
print('-' * 30)
totPrice = more1000 = lower = count = 0
cheaper = ''
while True:
    product = str(input('Product: '))
    price = float(input('Price: € '))
    count += 1
    totPrice += price
    if price > 1000:
        more1000 += 1
    if count == 1 or price < lower:
        lower = price
        cheaper = product
    option = ' '
    while option not in 'YN':
        option = str(input('Continue? [Y/N] ')).upper().strip()[0]
    if option == 'N':
        break
print(f'The total cost of the purchase is € {totPrice:.2f}.')
print(f'We have {more1000} products that cost more than € 1000.00.')
print(f'The cheaper product is {cheaper} that costs {lower:.2f}.')
