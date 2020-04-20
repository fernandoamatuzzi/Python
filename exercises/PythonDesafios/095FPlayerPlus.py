team = []
player = {}
matches = []
while True:
    player.clear()
    print('-' * 60)
    player['name'] = str(input('Player name: '))
    games = int(input(f'How many matches did {player["name"]} played: '))
    matches.clear()
    for c in range(0, games):
        matches.append(int(input(f'   How many goals in match {c+1}? ')))
    player['goals'] = matches[:]
    player['totgoals'] = sum(matches)
    team.append(player.copy())
    while True:
        r = str(input('Continue? [Y/N] ')).upper()[0]
        if r in 'YN':
            break
        print('ERROR! Please enter only Y or N.')
    if r == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 50)
for k, v in enumerate(team):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)
while True:
    search = int(input('Show data for which player? (999 to exit) '))
    if search == 999:
        break
    if search >= len(team):
        print(f'There is no player with code {search}. Please try again!')
    else:
        print(f' -- DATA FROM PLAYER {team[search]["name"]}: ')
        for i, g in enumerate(team[search]['goals']):
            print(f'   In match {i+1} scored {g} goals.')
    print('-' * 50)
print('<<< FINISHED >>>')
