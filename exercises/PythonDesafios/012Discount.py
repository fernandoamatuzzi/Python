price1 = float(input('The price of the product is € '))
disc = 5
price2 = price1 - (price1 * disc / 100)
print('The product that was costing € {:.2f}, after the discount of {}% is € {:.2f}.'.format(price1, disc, price2))
