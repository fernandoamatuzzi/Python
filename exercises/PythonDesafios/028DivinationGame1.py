from random import randint
from time import sleep
computer = randint(0, 5)
print('-=-' * 20)
print('I am gonna think in a number between 0 and 5. try to guess... ')
print('-=-' * 20)
player = int(input('What is the number? '))
print('LOADING...')
sleep(1.5)
if player == computer:
    print('Congratulations, you won!!')
else:
    print('You lose! My number is {}.'.format(computer))