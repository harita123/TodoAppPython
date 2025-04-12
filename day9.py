while True:
    user_action = input("Enter add, show, edit, complete or exit: ").strip()
    #user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip() # input("Enter a todo: ").strip() + "\n"
        if todo:
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                todos.append(todo + "\n")
            with open("todos.txt", 'w') as file:
                file.writelines(todos)

    elif user_action.startswith("show"):
        with open("todos.txt", 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            row = f'{index+1}.{item.strip()}'
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter the todo: ").strip() + "\n"
            todos[number] = new_todo.strip() + "\n"
            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1
            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            todos.pop(number)
            with open("todos.txt", 'w') as text_file:
                text_file.writelines(todos)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("You have entered an unknown command.")
print("Bye!!!")









