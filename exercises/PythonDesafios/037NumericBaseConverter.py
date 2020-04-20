num = int(input('Enter a integer number: '))
print('''Choose one conversion base:
[ 1 ] convert to BINARY
[ 2 ] convert to OCTAL
[ 3 ] convert to HEXADECIMAL''')
option = int(input('Your option: '))
if option == 1:
    print('{} converted to BINARY is {}.'.format(num, bin(num)[2:]))
elif option == 2:
    print('{} converted to OCTAL is {}.'.format(num, oct(num)[2:]))
elif option == 3:
    print('{} converted to HEXADECIMAL is {}.'.format(num, hex(num)[2:]))
else:
    print('Invalid option. Try again!')
