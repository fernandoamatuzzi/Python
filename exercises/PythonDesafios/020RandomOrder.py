from random import shuffle
s1 = input('First student: ')
s2 = input('Second student: ')
s3 = input('Third student: ')
s4 = input('Forth student: ')
array = [s1, s2, s3, s4]
shuffle(array)
print('The order is {}.'.format(array))
