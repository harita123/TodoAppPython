def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(todos_args, filepath='todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_args)

while True:
    user_action = input("Enter add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()
        if todo:
            todos = get_todos()
            todos.append(todo + "\n")
            write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            row = f'{index+1}.{item.strip()}'
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            print(f"Todo to edit: {todos[number].strip()}")  # Show the todo item
            new_todo = input("Enter a new todo: ").strip() + "\n"
            todos[number] = new_todo.strip() + "\n"
            write_todos(todos)
        except ValueError:
            print("Your command is invalid!!!")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1
            todos = get_todos()
            print(f"Todo completed: {todos[number].strip()}")  # Show the todo item
            todos.pop(number)
            write_todos(todos)
        except ValueError:
            print("Your command is invalid!!!")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("You have entered an unknown command!")

print("Bye!!!")
