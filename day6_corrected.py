while True:
    user_prompt = input("Enter add, show, edit, complete or exit: ")
    user_prompt = user_prompt.strip()

    match user_prompt:
        case "add":
            with open("todos.txt", "r") as file:
                todos = file.readlines() #open the existing file.
            todo = input("Enter a todo: ").strip() + "\n"
            todos.append(todo)
            with open("todos.txt", "w") as file:
                file.writelines(todos)
        case "show":
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                row = f'{index+1}.{item.strip()}'
                print(row)
        case "edit":
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            number = int(input("Enter the number of the todo you would like to edit: "))
            number = number-1
            new_todo = input("Enter the todo: ").strip() + "\n"
            todos[number] = new_todo.strip() + "\n"
            with open("todos.txt", "w") as file:
                file.writelines(todos)
        case "complete":
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            number = int(input("Enter the number of the todo you would like to mark as complete: "))
            number = number-1
            todos.pop(number)
            with open("todos.txt", "w") as file:
                file.writelines(todos)
        case "exit":
            break
        case _:
            print("You have entered an unknown command.")
