# Day 16 GUI

# todos = []

# from functions import get_todos, write_todos
from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")

print("It is:",now)

text = """
Principles of productivity:
Managing your inflow.
Systemizing everything that repeats.
"""

print(text)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = functions.get_todos()  # Using default params

        todos.append(todo + '\n')

        functions.write_todos(todos)  # Using default param

    elif user_action.startswith('show') or user_action.startswith('display'):

        todos = functions.get_todos()  # Using default params

        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            item = item.title()

            item = item.strip('\n')

            row = f"{index + 1}-{item}"  # call f"" string. index + 1 so that the index starts 1, 2, 3... instead of 0, 1, 2...
            print(row)

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()  # Using default params

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)  # negative 1 because in the case edit we had a negative 1

            functions.write_todos(todos)  # Using default param

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        except IndexError:
            print("There is no item with tha number.")
            continue

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1  # we use -1 to start the index at 0 as the user will not know pythin starts at 0

            todos = functions.get_todos()  # Using default params

            print('Here is the existing list: ', todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            print('Here is the modified list: ', todos)

            functions.write_todos(todos)  # Using default param

        except ValueError:
            print("Your command is not valid.")

            continue  # continue will break and re-run the program from the start

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")

print("Bye!")