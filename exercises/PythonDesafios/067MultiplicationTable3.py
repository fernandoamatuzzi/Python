while True:
    num = int(input('You want to see the Multiplication Table of which number? '))
    print('-' * 60)
    if num < 0:
        break
    for c in range(0, 11):
        print(f'{num} x {c:2} = {num*c}')
    print('-' * 60)
print('Multiplication Table finished. Thank you!')