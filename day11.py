"""Using functions."""

def get_todos():
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local




while True:
    user_action = input("Enter add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip() # input("Enter a todo: ").strip() + "\n"
        if todo:
            todos = get_todos()
            todos.append(todo + "\n")
            with open("todos.txt", 'w') as file_local:
                file_local.writelines(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            row = f'{index+1}.{item.strip()}'
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = get_todos()

            new_todo = input("Enter the todo: ").strip() + "\n"
            todos[number] = new_todo.strip() + "\n"
            with open("todos.txt", 'w') as file_local:
                file_local.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1
            todos = get_todos()
            todos.pop(number)
            with open("todos.txt", 'w') as file_local:
                file_local.writelines(todos)

        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("You have entered an unknown command.")
print("Bye!!!")