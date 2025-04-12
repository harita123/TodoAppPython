"""Using functions with arguments"""

def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Enter add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()
        if todo:
            todos = get_todos('todos.txt')
            todos.append(todo + "\n")
            write_todos('todos.txt', todos)

    elif user_action.startswith("show"):
        todos = get_todos('todos.txt')
        for index, item in enumerate(todos):
            row = f'{index+1}.{item.strip()}'
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos('todos.txt')
            new_todo = input("Enter a todo: ").strip() + "\n"
            todos[number] = new_todo.strip() + "\n"
            write_todos('todos.txt', todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1
            todos = get_todos('todos.txt')
            todos.pop(number)
            write_todos('todos.txt', todos)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("You have entered an unknown command!")

print("Bye!!!")


