a = int(input('First number: '))
b = int(input('Second number: '))
c = int(input('Third number: '))
# Checking the lowest
low = a
if b < a and b < c:
    low = b
if c < a and c < b:
    low = c
# Checking the highest
hig = a
if b > a and b > c:
    hig = b
if c > a and c > b:
    hig = c
print('The lowest number is {} and the highest is {}.'.format(low, hig))
