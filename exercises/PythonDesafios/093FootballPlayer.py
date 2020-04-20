player = {}
matches = []
player['name'] = str(input('Player name: '))
games = int(input(f'How many matches did {player["name"]} played: '))
for c in range(0, games):
    matches.append(int(input(f'   How many goals in match {c+1}? ')))
player['goals'] = matches[:]
player['totgoals'] = sum(matches)
print('-=' * 30)
for k, v in player.items():
    print(f'The field {k} has value {v}.')
print('-=' * 30)
print(f'The player {player["name"]} played {games} matches.')
for i, v in enumerate(player['goals']):
    print(f'   => In match {i+1} scored {v} goals.')
print(f'The total amount of goals was {player["totgoals"]}.')
