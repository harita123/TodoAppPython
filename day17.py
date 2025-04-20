"""Implementing the Add todo button"""


import functions
import FreeSimpleGUI as sg

label = sg.Text("Enter a Todo: ")
input = sg.InputText(tooltip="Type in a todo", key='todo')
button_add = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label, input, button_add]],
                   font=('Helvetica', 11))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()