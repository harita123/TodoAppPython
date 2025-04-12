def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file_local:
        todos = file_local.readlines()
        return todos

def write_todos(todos_args, filepath='todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_args)