print('Available bills: 1000, 500, 200, 100, 50, 20, 10')

number = input('Please enter the amount: ')

available_bank_notes = [1000, 500, 200, 100, 50, 20, 10]

max_number = 18800

if number[-1] != '0' or int(number) > max_number:
    print('Error!!!')
    exit()

number = int(number)
rest_of_money = max_number - number

result = []

for bank_note in available_bank_notes:
    if (rest_of_money / bank_note) >= 1:
        full = rest_of_money // bank_note
        rest = full - 10
        amount_banknotes = full - rest
        if rest < 0:
            result.append(str(abs(rest)) + '*' + str(bank_note))
            amount_banknotes = full

        rest_of_money = rest_of_money - (amount_banknotes * bank_note)
    else:
       result.append('10 *' + str(bank_note))
result.reverse() 
print(result)
