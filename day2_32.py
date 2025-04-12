todos = []

while True:
    user_action = input('Enter add, show or exit: ')
    user_action = user_action.strip() #strips away any spaces that the user may have added.
    match user_action:
        case 'add':
            todo = input('Enter a Todo: ')
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item.title())
        case 'exit':
            break
        case _:
            print('Hey you entered an unknown command.')

print('Bye')