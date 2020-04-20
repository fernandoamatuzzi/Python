def form(name='<unknown>', goals=0):
    print(f'The player {name} scored {goals} goal(s) in the championship.')


n = str(input('Player name: '))
g = str(input('Number of goals: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    form(goals=g)
else:
    form(n, g)
