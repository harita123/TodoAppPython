

todos = []

while True:
    user_action = input('Enter add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)

        case 'show':
            print('Here is your todo list:')
            for index, todo in enumerate(todos):
                print(f'{index+1}-{todo.capitalize()}')

        case 'edit':
            number = int(input('Enter the number of the todo you would like to edit: '))
            number = number-1
            new_todo = input('Enter a todo: ')
            todos[number] = new_todo

        case 'complete':
            number = int(input('Enter the number of the todo you would like to mark as complete: '))
            number = number - 1
            todos.pop(number)

        case 'exit':
            break

        case _:
            print('You have entered an unknown command.')