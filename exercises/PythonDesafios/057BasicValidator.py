g = str(input('Enter your gender: [M/F] ')).upper()[0].strip()
while g not in 'MmFf':
    g = str(input('Invalid entry! Enter your gender: [M/F] ')).upper()[0].strip()
print('Thank you! Gender {} registered with success.'.format(g))
