waiting_list = ['Ben', 'Sen', 'John']

#1.Ben
#2.John
#3.Sen

waiting_list.sort()

for index, item in enumerate(waiting_list):
    print(f'{index+1}. {item.capitalize()}')

buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(first, second, third)