from time import sleep


def higher(*values):
    count = highest = 0
    print('-=' * 20)
    print('Analyzing data...')
    for num in values:
        print(f'{num} ', end='')
        sleep(0.4)
        if count == 0:
            highest = num
        elif num > highest:
            highest = num
        count += 1
    print(f'- We received {len(values)} numbers.')
    print(f'The highest number is {highest}.')


higher(2, 9, 4, 5, 7, 1)
higher(4, 7, 0)
higher(1, 2)
higher(6)
higher()
