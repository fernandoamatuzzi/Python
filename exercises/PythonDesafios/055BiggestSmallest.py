heavier = 0
lighter = 0
for p in range(1, 6):
    weight = float(input('Weight of the person {}: '.format(p)))
    if p == 1:
        heavier = weight
        lighter = weight
    else:
        if weight > heavier:
            heavier = weight
        if weight < lighter:
            lighter = weight
print('The heaviest weight is {}Kg.'.format(heavier))
print('The lighter weight is {}Kg.'.format(lighter))
