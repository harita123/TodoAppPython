password = input('Enter a password:')

while password != 'pass123':
    password = input('Enter a password:')

print('Password is correct.')

cheque_start = input('Enter the starting cheque number:')
cheque_end = input('Enter the ending cheque number:')

while cheque_start <= cheque_end:
    print(cheque_start)
    cheque_start = cheque_start+1