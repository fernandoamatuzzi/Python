sentence = str(input('Enter a sentence: ')).strip().upper()
words = sentence.split()
together = ''.join(words)
inverted = ''
inverted = together[::-1]
'''for letter in range(len(together) - 1, -1, -1):
    inverted += together[letter]'''
print('The inverted of {} is {}.'.format(together, inverted))
if inverted == together:
    print('There is a palindrome!')
else:
    print('There is NO palindrome!')
