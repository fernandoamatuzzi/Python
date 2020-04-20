people = []
person = {}
sum = average = 0
while True:
    person.clear()
    person['name'] = str(input('Name: '))
    while True:
        person['gender'] = str(input('Gender [M/F]: ')).upper()[0]
        if person['gender'] in 'MF':
            break
        print('ERROR! Please enter only M or F.')
    person['age'] = int(input('Age: '))
    sum += person['age']
    people.append(person.copy())
    while True:
        r = str(input('Continue? [Y/N] ')).upper()[0]
        if r in 'YN':
            break
        print('ERROR! Please enter only Y or N.')
    if r == 'N':
        break
print('-=' * 30)
print(f'A) In total we have {len(people)} people registered.')
average = sum / len(people)
print(f'B) The average age is {average:5.2f} years old.')
print('C) The women registered were ', end='')
for p in people:
    if p['gender'] in 'F':
        print(f'{p["name"]} ', end='')
print()
print('D) People over the average age: ', end='')
for p in people:
    if p['age'] >= average:
        print('    ', end='')
        for k, v in p.items():
            print(f' -> {k} = {v}; ', end='')
        print()
print('      <<< FINISHED >>>')
