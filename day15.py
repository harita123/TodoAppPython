"""Adding a date feature to the application."""


import functions
import time

now = time.strftime("Date: %b - %d - %Y Time: %H:%M:%S")
print(now)

while True:
    user_action = input("Enter add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()
        todos = functions.get_todos()
        todos.append(todo + "\n")
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            row = f'{index+1}.{item.strip()}'
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()
            print(f"Todo to edit: {todos[number].strip()}")
            new_todo = input("Enter a todo: ")
            todos[number] = new_todo.strip()+"\n"
            functions.write_todos(todos)
        except ValueError:
            print("Your command is invalid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number-1
            todos = functions.get_todos()
            print(f"Todo to complete: {todos[number].strip()}")
            todos.pop(number)
            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("You have entered an unknown command!!!")

print("Bye!!!")
