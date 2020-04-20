from random import randint
from time import sleep
from operator import itemgetter
dice = {'player1': randint(1, 6),
        'player2': randint(1, 6),
        'player3': randint(1, 6),
        'player4': randint(1, 6)}
ranking = list()
print('Numbers drawn:')
for k, v in dice.items():
    print(f'{k} played {v} in the dice.')
    sleep(1)
ranking = sorted(dice.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
print('  ======== RANKING ========')
for i, v in enumerate(ranking):
    print(f'   {i+1} place: {v[0]} with {v[1]}')
    sleep(1)
