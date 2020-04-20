expr = str(input('Enter an expression: '))
pile = []
for simb in expr:
    if simb == '(':
        pile.append('(')
    elif simb == ')':
        if len(pile) > 0:
            pile.pop()
        else:
            pile.append(')')
            break
if len(pile) == 0:
    print('You expression is valid!')
else:
    print('Your expression is invalid!')
