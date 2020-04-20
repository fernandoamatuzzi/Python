from datetime import date
birth = int(input('Enter your birth year: '))
year = date.today().year
age = year - birth
if age < 18:
    time = 18 - age
    nyear = year + time
    print('You are {} years old and need to present yourself to the Army in {} years.'.format(age, time))
    print('You will present yourself in {}.'.format(nyear))
elif age == 18:
    print('You are {} years old and must present yourself to the Army this year!'.format(age))
else:
    time = age - 18
    nyear = year - time
    print('You are {} years old and should have presented yourself to the Army {} years ago.'.format(age, time))
    print('You should have presented yourself in {}.'.format(nyear))
