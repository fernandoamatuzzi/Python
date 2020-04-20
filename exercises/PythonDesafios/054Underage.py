from datetime import date
totlegal = 0
totunder = 0
year = date.today().year
for people in range(1, 8):
    birth = int(input('Year of birth of person {}: '.format(people)))
    age = year - birth
    if age >= 18:
        totlegal += 1
    else:
        totunder += 1
print('In total we have {} people of legal age.'.format(totlegal))
print('And also, we have {} people underage.'.format(totunder))
