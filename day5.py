
todos = []

while True:
    user_action = input('Enter add, show, edit or exit: ')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)

        case 'show':
            if not todos:
                print('No todos exit.')
            else:
                print('Here is your todo list: ')
                for index, item in enumerate(todos):
                    print(f"{index + 1}. {item.strip().capitalize()}")  # Ensure clean formatting

        case 'edit':
            number = int(input('Enter the number of todo you want to edit: '))
            number = number - 1
            new_todo = input('Enter a todo: ')
            todos[number] = new_todo

        case 'exit':
            break

        case _:
            print('You have entered an unknown command.')