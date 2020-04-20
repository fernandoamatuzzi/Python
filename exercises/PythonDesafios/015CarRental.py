days = int(input('How many days did you rent the car? '))
km = float(input('How many kilometers did you drive? '))
dayfee = 60
kmfee = 0.15
price = (days * dayfee) + (km * kmfee)
print('You rented the car for {} days and drove {}km, so the final price is €{:.2f}.'.format(days, km, price))
