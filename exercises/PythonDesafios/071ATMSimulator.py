print('=' * 45)
print('{:^45}'.format('THE GOOD BANK'))
print('=' * 45)
withdraw = int(input('How much you would like to withdraw? € '))
total = withdraw
note = 50
totNote = 0
while True:
    if total >= note:
        total -= note
        totNote += 1
    else:
        print(f'Total of {totNote} notes of € {note}.')
        if note == 50:
            note = 20
        elif note == 20:
            note = 10
        elif note == 10:
            note = 1
        totNote = 0
        if total == 0:
            break
print('=' * 45)
print('Thank you! Have a nice day!')
