from random import randint
from time import sleep
print('-' * 30)
print(f'{"EURO MILLION":^30}')
print('-' * 30)
lyst = []
games = []
quant = int(input('How many games do you want to draw? '))
tot = 1
while tot <= quant:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lyst:
            lyst.append(num)
            count += 1
        if count >= 6:
            break
    lyst.sort()
    games.append(lyst[:])
    lyst.clear()
    tot += 1
print('-=' * 3, f' RAFFLING {quant} GAMES ', '=-' * 3)
for i, l in enumerate(games):
    print(f'Game {i+1}: {l}')
    sleep(1)
print('-=' * 4, '< GOOD LUCK! >', '=-' * 4)
