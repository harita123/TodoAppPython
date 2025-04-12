"""Storing data in text files"""

todos = []

while True:
    user_prompt = input('Enter - add, show, edit, complete, or exit: ')
    user_prompt = user_prompt.strip()

    match user_prompt:
        case 'add':
            todo = input('Enter a todo: ')
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
            for index, item in enumerate(todos):
                print(f'{index + 1}.{item.capitalize()}')
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                print(f'{index+1}.{item.capitalize()}')
        case 'edit':
            for index, item in enumerate(todos):
                print(f'{index+1}.{item.capitalize()}')
            number = int(input('Enter the todo you would like to edit: '))
            number = number-1
            new_todo = input('Enter the todo: ')
            todos[number] = new_todo
        case 'complete':
            for index, item in enumerate(todos):
                print(f'{index+1}.{item.capitalize()}')
            number = int(input('Enter the todo you would like to complete: '))
            number = number-1
            todos.pop(number)
        case 'exit':
            break
        case _:
            print('You have entered an unknown command.')