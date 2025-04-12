while True:
    user_prompt = input("Enter add, show, edit, complete or exit: ").strip()

    match user_prompt:
        case "add":
            with open("todos.txt", "r") as file:
                todos = file.readlines()  # Open the existing file.
            todo = input("Enter a todo: ").strip() + "\n"  # Ensure newline
            todos.append(todo)
            with open("todos.txt", "w") as file:
                file.writelines(todos)  # Write back with proper newlines

        case "show":
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                row = f'{index + 1}. {item.strip()}'
                print(row)

        case "edit":
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            number = int(input("Enter the number of the todo you would like to edit: ")) - 1
            new_todo = input("Enter the new todo: ").strip() + "\n"  # Ensure newline
            todos[number] = new_todo
            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "complete":
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            number = int(input("Enter the number of the todo you would like to mark as complete: ")) - 1
            todos.pop(number)
            with open("todos.txt", "w") as file:
                file.writelines(todos)  # Write back with proper newlines

        case "exit":
            break

        case _:
            print("You have entered an unknown command.")



