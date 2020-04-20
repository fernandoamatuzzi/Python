from datetime import date
birth = int(input('Enter the year of birth: '))
age = date.today().year - birth
print('The athlete is \33[1;30m{}\33[m years old.'.format(age))
if age <= 9:
    print('Category: \33[4;1;33mLITTLE')
elif age <= 14:
    print('Category: \33[4;1;32mKIDS')
elif age <= 19:
    print('Category: \33[4;1;36mJUNIORS')
elif age <= 25:
    print('Category: \33[4;1;35mSENIORS')
else:
    print('Category: \33[4;1;34mMASTERS')
