print('Available bills: 1000, 500, 200, 100, 50, 20, 10')

number = input('Please enter the amount: ')

available_bank_notes = [1000, 500, 200, 100, 50, 20, 10]

if number[-1] != '0':
    print('Error!!!')
    exit()

number = int(number)

for bank_note in available_bank_notes:
    if (number / bank_note) >= 1:
        full = number // bank_note
        number = number - (full * bank_note)
        print(str(full) + '*' + str(bank_note))
