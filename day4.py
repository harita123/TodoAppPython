todos = []

while True:
    user_action = input('Enter add, show, edit or exit: ')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a to do: ')
            todos.append(todo)

        case 'show':
            for item in todos:
                print(item.title())

        case 'edit':
            number = int(input('Number of the todo item to edit: '))
            number = number -1
            new_todo = input('Enter a todo: ')
            todos[number] = new_todo
            print(new_todo)

        case 'exit':
            break

        case _:
            print('You have entered an unknown command')