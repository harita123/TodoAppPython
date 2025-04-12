"""Lecture 133 - Modules. We can organize code into modules, by transferring code to
a different file. The code can be called into the main program file using import. Here
we will be shifting the two functions to a seperate python file and calling the functions here.
This is called Modules in python."""

from functions import get_todos, write_todos



while True:
    user_action = input("Enter add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()
        if todo:
            todos = get_todos()
            todos.append(todo + '\n')
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
            print(number)
            todos = get_todos()
            new_todo = input("Enter a todo: ").strip()+"\n"
            todos[number] = new_todo.strip()+'\n'
            write_todos(todos)
        except ValueError:
            print("Your command is invalid.")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1
            todos = get_todos()
            todos.pop(number)
            write_todos(todos)
        except IndexError:
            print("There is no item with that number")

    elif user_action.startswith("exit"):
        break

    else:
        print("You have entered an unknown command")

print("Bye!!!")


