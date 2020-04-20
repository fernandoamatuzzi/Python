from random import randint
from time import sleep


def draw(list):
    print('Drawing 5 numbers: ')
    for count in range(0, 5):
        n = randint(1, 10)
        list.append(n)
        print(f'{n} ', end='')
        sleep(0.4)
    print('Done!!')


def evenSum(list):
    sum = 0
    for value in list:
        if value % 2 == 0:
            sum += value
    print(f'The sum of the even numbers from {list} is {sum}.')


numbers = []
draw(numbers)
evenSum(numbers)
