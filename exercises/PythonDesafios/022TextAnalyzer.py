name = str(input('Enter your full name: ')).strip()
print('Your full name is {}.'.format(name))
print('Uppercase is {}.'.format(name.upper()))
print('Lowercase is {}.'.format(name.lower()))
print('Your full name has {} letters.'.format(len(name) - name.count(' ')))
print('Your first name has {} letters.'.format(name.find(' ')))
separate = name.split()
print('Your first name has {} letters.'.format(len(separate[0])))