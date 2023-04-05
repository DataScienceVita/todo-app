FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
        Read a text file and return the list of
        todos items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local
# function is recommended to have two spaces
# function is recommended to have two spaces


# print(help(get_todos))  # This prints out the doc strings


def write_todos(todos_arg, filepath="todos.txt"):  # default param are at the end
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
    # no return because the write method modifies and does not need to return


print("Hello from functions")