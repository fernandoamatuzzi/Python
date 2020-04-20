num = ('zero', 'one', 'two', 'three', 'four', 'five',
       'six', 'seven', 'eight', 'nine', 'ten',
       'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
       'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
enter = int(input('Enter a number between 0 and 20: '))
while enter < 0 or enter > 20:
    enter = int(input('Enter a number between 0 and 20: '))
print(f'You entered the number {num[enter]}.')
