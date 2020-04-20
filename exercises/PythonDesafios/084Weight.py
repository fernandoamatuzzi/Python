main = []
temp = []
heavier = lighter = 0
while True:
    temp.append(str(input('Name: ')))
    temp.append(float(input('Weight: ')))
    if len(main) == 0:
        heavier = lighter = temp[1]
    else:
        if temp[1] > heavier:
            heavier = temp[1]
        if temp[1] < lighter:
            lighter = temp[1]
    main.append(temp[:])
    temp.clear()
    r = str(input('Continue? [Y/N] ')).upper().strip()[0]
    if r in 'N':
        break
print('-=' * 30)
print(f'You entered {len(main)} people.')
print(f'The heavier weight is {heavier}Kg. Weight of ', end='')
for p in main:
    if p[1] == heavier:
        print(f'[{p[0]}] ', end='')
print()
print(f'The lighter weight is {lighter}Kg. Weight of ', end='')
for p in main:
    if p[1] == lighter:
        print(f'[{p[0]}] ', end='')
