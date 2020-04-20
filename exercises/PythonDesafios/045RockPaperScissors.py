from random import randint
from time import sleep
items = ('Rock', 'Paper', 'Scissors')
comp = randint(0, 1)
print('''Options:
[ 0 ] ROCK
[ 1 ] PAPER
[ 2 ] SCISSORS''')
player = int(input('Which is your option? '))
if player != 0 and player != 1 and player != 2:
    print('\33[1;31;40m{:-^30}'.format(' (INVALID PLAY!) '), end='')
else:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!')
    sleep(0.5)
    print('-=-' * 10)
    print('Computer --> \33[1m{}\33[m'.format(items[comp]))
    print('Player --> \33[1m{}\33[m'.format(items[player]))
    print('-=-' * 10)
    if comp == 0:
        if player == 0:
            print("\33[1;33;40m{:-^30}".format(" (IT'S A DRAW!) "), end='')
        elif player == 1:
            print('\33[1;34;40m{:-^30}'.format(' (YOU WIN!) '), end='')
        elif player == 2:
            print('\33[1;35;40m{:-^30}'.format(' (YOU LOSE!) '), end='')
    elif comp == 1:
        if player == 0:
            print('\33[1;35;40m{:-^30}'.format(' (YOU LOSE!) '), end='')
        elif player == 1:
            print("\33[1;33;40m{:-^30}".format(" (IT'S A DRAW!) "), end='')
        elif player == 2:
            print('\33[1;34;40m{:-^30}'.format(' (YOU WIN!) '), end='')
    elif comp == 2:
        if player == 0:
            print('\33[1;34;40m{:-^30}'.format(' (YOU WIN!) '), end='')
        elif player == 1:
            print('\33[1;35;40m{:-^30}'.format(' (YOU LOSE!) '), end='')
        elif player == 2:
            print("\33[1;33;40m{:-^30}".format(" (IT'S A DRAW!) "), end='')
