import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a To-Do:")
input_box = sg.InputText(tooltip="Type in a todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()

#https://github.com/harita123/TodoAppPython.git