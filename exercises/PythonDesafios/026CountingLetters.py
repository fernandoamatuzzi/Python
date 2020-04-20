str = str(input('Please type a sentence: ')).strip().lower()
print('Your sentence is: "{}".'.format(str))
print("The letter 'a' occurs {} time(s).".format(str.lower().count('a')))
print("The first time letter 'a' occurs is in the position {}.".format(str.find('a')+1))
print("The last letter 'a' occurs in the position {}.".format(str.rfind('a')+1))


