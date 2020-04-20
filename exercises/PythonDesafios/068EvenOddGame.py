from random import randint
print('=-=' * 21)
print('Playing even or odd')
print('=-=' * 21)
v = 0
while True:
    option = ' '
    while option not in 'EO':
        option = str(input('Even or Odd? [E/O] ')).upper().strip()[0]
    player = int(input('Say a number: '))
    computer = randint(0, 10)
    total = player + computer
    print('~' * 63)
    print(f'You played {player} and the computer played {computer}. The total is {total} -> ', end='')
    print('EVEN!' if total % 2 == 0 else 'ODD!')
    print('~' * 63)
    if option == 'E':
        if total % 2 == 0:
            print('You win!')
            v += 1
        else:
            print('You lose!')
            break
    elif option == 'O':
        if total % 2 == 1:
            print('You win!')
            v += 1
        else:
            print('You lose!')
            break
    print("Let's play again!")
    print('-' * 63)
print(f'Game over!! You won {v} times.')
