todos = []

while True:
    user_action = input('Enter add, show, edit or exit: ')
    user_action = user_action.strip().lower()  # Normalize input for consistency

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo.strip())  # Strip extra spaces when adding
            print(f"Added todo: {todo.strip()}")

        case 'show':
            if not todos:
                print("No todos to show.")
            else:
                print("Here is your todo list:")
                for index, item in enumerate(todos):
                    print(f"{index + 1}. {item.strip()}")  # Ensure clean formatting

        case 'edit':
            if not todos:
                print("No todos to edit.")
            else:
                try:
                    print("Current todos:")
                    for index, item in enumerate(todos):
                        print(f"{index + 1}. {item.strip()}")
                    number = int(input('Enter the number of the todo you want to edit: '))
                    if 1 <= number <= len(todos):
                        new_todo = input('Enter a new todo: ')
                        todos[number - 1] = new_todo.strip()
                        print(f"Todo {number} updated to: {new_todo.strip()}")
                    else:
                        print("Invalid todo number.")
                except ValueError:
                    print("Please enter a valid number.")

        case 'exit':
            print("Goodbye!")
            break

        case _:
            print('You have entered an unknown command.')
