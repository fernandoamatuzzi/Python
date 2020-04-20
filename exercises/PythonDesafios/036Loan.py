house = float(input('Price of the house: €'))
salary = float(input('Salary per month: €'))
year = int(input('In how many years you would like to pay the house? '))
inst = house / (year * 12)
print('To buy a house of €{:.2f}, the monthly installments are going to be €{:.2f} during {} years.'.format(house, inst, year))
if inst > salary * (30 / 100):
    print('Unfortunately your loan was NOT approved.')
else:
    print('Your loan was APPROVED!')
