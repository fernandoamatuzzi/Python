from time import sleep


def counter(start, end, pace):
    if pace < 0:
        pace *= -1
    if pace == 0:
        pace = 1
    print('-=' * 20)
    print(f'Counting from {start} to {end}, {pace} by {pace}:')
    sleep(1.5)
    if start < end:
        count = start
        while count <= end:
            print(f'{count} ', end='')
            sleep(0.5)
            count += pace
        print('End!')
    else:
        count = start
        while count >= end:
            print(f'{count} ', end='')
            sleep(0.5)
            count -= pace
        print('End!')


counter(1, 10, 1)
counter(10, 0, 2)
print('-=' * 20)
print('Now is your turn to personalize the counter!')
s = int(input('Start: '))
e = int(input('End:   '))
p = int(input('Pace:  '))
counter(s, e, p)
