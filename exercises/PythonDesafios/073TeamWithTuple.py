teams = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
         'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense',
         'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('-=' * 30)
print(f'List of teams: {teams}')
print('-=' * 30)
print(f'The first five are {teams[0:5]}.')
print('-=' * 30)
print(f'The last four are {teams[-4:]}.')
print('-=' * 30)
print(f'Alphabetical order: {sorted(teams)}')
print('-=' * 30)
print(f"Chapecoense is at the {teams.index('Chapecoense') + 1}ª position.")
print('-=' * 30)
