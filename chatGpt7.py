todos = []

while True:
    user_prompt = input('Enter add, show, edit, complete or exit: ').strip()

    match user_prompt:
        case 'add':
            todo = input('Enter a todo: ').strip()
            with open('todos.txt', 'a') as file:  # Append mode
                file.write(todo + '\n')  # Add newline for proper formatting
            print(f'Todo "{todo}" added.')

        case 'show':
            with open('todos.txt', 'r') as file:  # Read mode
                todos = file.readlines()
            if todos:
                print("Your todos:")
                for index, item in enumerate(todos):
                    print(f'{index + 1}. {item.strip().capitalize()}')
            else:
                print("No todos found.")

        case 'edit':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            if todos:
                try:
                    number = int(input("Enter the todo number you would like to edit: "))
                    if 1 <= number <= len(todos):
                        new_todo = input("Enter the new todo: ").strip()
                        todos[number - 1] = new_todo + '\n'
                        with open('todos.txt', 'w') as file:
                            file.writelines(todos)
                        print(f"Todo {number} updated to: {new_todo}")
                    else:
                        print("Invalid todo number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No todos found to edit.")

        case 'complete':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            if todos:
                try:
                    number = int(input('Enter the todo number you would like to mark as complete: '))
                    if 1 <= number <= len(todos):
                        removed_todo = todos.pop(number - 1).strip()
                        with open('todos.txt', 'w') as file:
                            file.writelines(todos)
                        print(f'Todo "{removed_todo}" marked as complete and removed.')
                    else:
                        print("Invalid todo number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No todos found to complete.")

        case 'exit':
            print("Exiting the program. Goodbye!")
            break

        case _:
            print('You have entered an unknown command.')
