from random import randint
from time import sleep
from typing import Any, Union

computer = randint(0, 10)
print('-=-' * 20)
print('I am gonna think in a number between 0 and 10. Try to guess... ')
print('-=-' * 20)
right = False
guess = 0
while not right:
    player = int(input('What is your guess? '))
    guess += 1
    if player == computer:
        right = True
    else:
        if player < computer:
            print('More... Try again! ')
        elif player > computer:
            print('Less... Try again! ')
print('Congratulations! You needed {} guesses to get the right number!'.format(guess))
