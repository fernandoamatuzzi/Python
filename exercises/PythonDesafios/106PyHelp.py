from time import sleep

c = ('\033[m',  # 0 - no color
     '\033[0;30;41m',  # 1 - red
     '\033[0;30;42m',  # 2 - green
     '\033[0;30;43m',  # 3 - yellow
     '\033[0;30;44m',  # 4 - blue
     '\033[0;30;45m',  # 5 - purple
     '\033[7;30m',  # 6 - white
     );


def hellp(com):
    title(f'Accessing the manual of the command \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def title(msg, color=0):
    size = len(msg) + 4
    print(c[color], end='')
    print('~' * size)
    print(f'  {msg}')
    print('~' * size)
    print(c[0], end='')
    sleep(1)


command = ''
while True:
    title('PyHELP SYSTEM', 2)
    command = str(input('Function or Library: '))
    if command.upper() == 'END':
        break
    else:
        hellp(command)
title('See you soon!', 1)
