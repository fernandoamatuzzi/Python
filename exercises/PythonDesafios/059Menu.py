from time import sleep
n1 = int(input('First number: '))
n2 = int(input('Second number: '))
option = 0
while option != 5:
    print('Your numbers are {} and {}.'.format(n1, n2))
    print('''Which option do you want to do:
    [ 1 ] Sum
    [ 2 ] Multiply
    [ 3 ] Highest value
    [ 4 ] New numbers
    [ 5 ] Exit program''')
    option = int(input('>>>>>>> Your option: '))
    if option == 1:
        sum = n1 + n2
        print('The sum of {} and {} is {}.'.format(n1, n2, sum))
    elif option == 2:
        mul = n1 * n2
        print('The multiplication of {} times {} is {}.'.format(n1, n2, mul))
    elif option == 3:
        if n1 > n2:
            print('The highest value between {} and {} is {}.'.format(n1, n2, n1))
        elif n1 < n2:
            print('The highest value between {} and {} is {}.'.format(n1, n2, n2))
        else:
            print('Both numbers have the same value.')
    elif option == 4:
        print('Enter new numbers:')
        n1 = int(input('First number: '))
        n2 = int(input('Second number: '))
    elif option == 5:
        print('Finalizing...')
    else:
        print('Invalid option. Try again!')
    print('=-=' * 10)
sleep(1.5)
print('Program ended. Thank you!')
