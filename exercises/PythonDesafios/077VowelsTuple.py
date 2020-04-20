words = ('learn', 'programming', 'language', 'python', 'course',
         'study', 'practice', 'work', 'market', 'programmer', 'future')
for w in words:
    print(f'\nIn the word {w.upper()} we have ', end='')
    for letter in w:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
