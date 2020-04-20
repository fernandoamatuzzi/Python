from datetime import date
year = int(input('Which year do you want to check? Enter 0 to check the current year. '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('{} is a leap year!'.format(year))
else:
    print('{} is not a leap year.'.format(year))
