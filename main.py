# Day 1 print, variables, function, list

# user_prompt = "Enter a todo:"
#
# # todo1 = input(Enter a todo:")
#
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)
#
# todos = [todo1, todo2, todo3]
# print(todos)
# print(type(todos))

# Day 2 while-loop
#
# user_prompt = "Enter a todo: "
# todos = []
#
# # while 2 > 1:
# while True:
#     todo1 = input(user_prompt)
#     todos.append(todo1)
#     print(todos, "Next...")

# Day 3 match & case

# todos = []
#
# while True:
#     user_action = input("Type add, show, edit or exit: ")
#     user_action = user_action.strip()
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo: ")
#             todos.append(todo)
#         case 'show' | 'display':
#             # print(todos)
#             for items in todos:
#                 items = items.title()
#                 print(items)
#         case 'exit':
#             break
#         case anyvariable: #on-demand variable. case _: is conventional
#             print("Please enter one of the menu command")
#
# print(("Bye!"))

# Day 4 type conversion & tuples

todos = []

# while True:
#     user_action = input("Type add, show, edit or exit: ")
#     user_action = user_action.strip()
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo: ")
#             todos.append(todo)
#         case 'show' | 'display':
#             # print(todos)
#             for items in todos:
#                 items = items.title()
#                 print(items)
#         case 'exit':
#             break
#         case 'edit':
#             number = int(input("Number of the todo to edit: "))
#             number = number - 1
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo
#         case anyvariable: #on-demand variable. case _: is conventional
#             print("Please enter one of the menu command")
#
# print(("Bye!"))
#
# # python console - todos = ['clean', 'throw', 'prepare'], todos[1]


# Day 5 enumerate, remove, pop

# todos = []
#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo: ")
#             todos.append(todo)
#         case 'show' | 'display':
#             # print(todos)
#             for index, items in enumerate(todos):
#                 items = items.title()
#                 # index = index + 1 add the + 1 in the f string
#                 # print(index, '-', items) # this will have a space like this '1 - Hey', but we want '1-Hey' with no spaces between the dash
#                 row = f"{index + 1}-{items}" #call f"" string. index + 1 so that the index starts 1, 2, 3... instead of 0, 1, 2...
#                 print(row)
#             #print("Hello", index, item) -- once the program shows the items it will print Hello, the number of the last index and display the last item in the list as it exit out the loop
#             # print("Length is  ", index)
#             # print(f"Length is {index + 1}")
#             # a better way of the above code of getting the length of the index is:
#             # print(len(todos))
#         case 'complete':
#             number = int(input("Number of the todo to complete: "))
#             pop_number = number
#             todos.pop(number - 1) # negative 1 because in the case edit we had a negative 1
#         case 'exit':
#             break
#         case 'edit':
#             number = int(input("Number of the todo to edit: "))
#             number = number - 1 # we use -1 to start the index at 0 as the user will not know pythin starts at 0
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo
#         case anyvariable: #on-demand variable. case _: is conventional
#             print("Please enter one of the menu command")
#
#
# print(("Bye!"))

# python console - todos = ['clean', 'throw', 'prepare'], todos[1]
# a = enumerate(["a", "b", "c", "d"])
# >>> a -- will return an error. because the object itself cannot display
# >>> list(a) -- this can be displayed

#  enumerate is getting items from a tuple


# # Day 6 storing in text file
#
# #todos = []
#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo: ") + "\n"
#             file = open('todos.txt', 'r')
#             todos = file.readlines()
#             file.close() # should always good as coding practice
#
#             todos.append(todo)
#
#             file = open('todos.txt', 'w') # create a todos.txt file in the same directory as the main.py first
#             file.writelines(todos)
#             file.close()  # should always good as coding practice
#         case 'show' | 'display':
#             # print(todos)
#             file = open('todos.txt', 'r')
#             todos = file.readlines()
#             file.close()
#
#             for index, items in enumerate(todos):
#                 items = items.title()
#                 # index = index + 1 add the + 1 in the f string
#                 # print(index, '-', items) # this will have a space like this '1 - Hey', but we want '1-Hey' with no spaces between the dash
#                 row = f"{index + 1}-{items}" #call f"" string. index + 1 so that the index starts 1, 2, 3... instead of 0, 1, 2...
#                 print(row)
#             #print("Hello", index, item) -- once the program shows the items it will print Hello, the number of the last index and display the last item in the list as it exit out the loop
#             # print("Length is  ", index)
#             # print(f"Length is {index + 1}")
#             # a better way of the above code of getting the length of the index is:
#             # print(len(todos))
#         case 'complete':
#             number = int(input("Number of the todo to complete: "))
#             pop_number = number
#             todos.pop(number - 1) # negative 1 because in the case edit we had a negative 1
#         case 'exit':
#             break
#         case 'edit':
#             number = int(input("Number of the todo to edit: "))
#             number = number - 1 # we use -1 to start the index at 0 as the user will not know pythin starts at 0
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo
#         case anyvariable: #on-demand variable. case _: is conventional
#             print("Please enter one of the menu command")
#
#
# print(("Bye!"))

# In day 6 we removed the todos = [] "List" and use the todos = file.readlines() in the 'add' section as our so called "list
# ths issue is now the "show" section cannot display the todos or it cannot enumerate the todos ist anymore because the todos is not declared
# So we have to include the same logic in the "show" section

# file.readlines() is equal to creating a list = []
# ex file = open(r"C:\User\Veo\Downloads\todos_example.txt", 'r') use the 'r' in front to avoid confusing python with special character like \n or \t


# Day 7 comprehension, remove double spaces, batch operation

# #todos = []
#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo: ") + "\n"
#             file = open('todos.txt', 'r')
#             todos = file.readlines()
#             file.close() # should close always as a good coding practice
#
#             todos.append(todo)
#
#             file = open('todos.txt', 'w') # create a todos.txt file in the same directory as the main.py first
#             file.writelines(todos)
#             file.close()  # should always good as coding practice
#         case 'show' | 'display':
#             file = open('todos.txt', 'r')
#             todos = file.readlines()
#             file.close()
#
#             # # 1st option - learning how to remove the '\n' so when we print it doesn't double-space
#             # new_todos = []
#             # for item in todos:
#             #     new_item = item.strip('\n')
#             #     new_todos.append(new_item)
#
#             # 2nd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#             # List Comprehension
#             # new_todos = [item.strip('\n') for item in todos]
#
#             # for index, item in enumerate(todos):
#             for index, item in enumerate(new_todos):
#                 item = item.title()
#
#                 # # 3rd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#                 item = item.strip('\n')
#
#                 # index = index + 1 add the + 1 in the f string
#                 # print(index, '-', items) # this will have a space like this '1 - Hey', but we want '1-Hey' with no spaces between the dash
#
#                 row = f"{index + 1}-{item}" #call f"" string. index + 1 so that the index starts 1, 2, 3... instead of 0, 1, 2...
#                 print(row)
#
#             #print("Hello", index, item) -- once the program shows the items it will print Hello, the number of the last index and display the last item in the list as it exit out the loop
#             # print("Length is  ", index)
#             # print(f"Length is {index + 1}")
#             # a better way of the above code of getting the length of the index is:
#             # print(len(todos))
#
#         case 'complete':
#             number = int(input("Number of the todo to complete: "))
#             pop_number = number
#             todos.pop(number - 1) # negative 1 because in the case edit we had a negative 1
#         case 'exit':
#             break
#         case 'edit':
#             number = int(input("Number of the todo to edit: "))
#             number = number - 1 # we use -1 to start the index at 0 as the user will not know pythin starts at 0
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo
#         case anyvariable: #on-demand variable. case _: is conventional
#             print("Please enter one of the menu command")
#
#
# print(("Bye!"))


# Day 8 content manager

# todos = []

# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo: ") + "\n"
#
#             # the open and close code below can be more efficient
#             # using the 'with' function
#
#             # file = open('todos.txt', 'r')
#             # todos = file.readlines()
#             # file.close() # should close always as a good coding practice
#
#             #  with - no need to close file as it will do it automatically
#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()
#
#
#             todos.append(todo)
#
#             # will replace the codes below with the with function to open file and automatically close file
#
#             # file = open('todos.txt', 'w') # create a todos.txt file in the same directory as the main.py first
#             # file.writelines(todos)
#             # file.close()  # should always good as coding practice
#
#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#         case 'show' | 'display':
#             # file = open('todos.txt', 'r')
#             # todos = file.readlines()
#             # file.close()
#
#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()
#
#
#             # # 1st option - learning how to remove the '\n' so when we print it doesn't double-space
#             # new_todos = []
#             # for item in todos:
#             #     new_item = item.strip('\n')
#             #     new_todos.append(new_item)
#
#             # 2nd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#             # List Comprehension
#             new_todos = [item.strip('\n') for item in todos]
#
#             # for index, item in enumerate(todos):
#             for index, item in enumerate(new_todos):
#                 item = item.title()
#
#                 # # 3rd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#                 item = item.strip('\n')
#
#                 # index = index + 1 add the + 1 in the f string
#                 # print(index, '-', items) # this will have a space like this '1 - Hey', but we want '1-Hey' with no spaces between the dash
#
#                 row = f"{index + 1}-{item}"  #call f"" string. index + 1 so that the index starts 1, 2, 3... instead of 0, 1, 2...
#                 print(row)
#
#             #print("Hello", index, item) -- once the program shows the items it will print Hello, the number of the last index and display the last item in the list as it exit out the loop
#             # print("Length is  ", index)
#             # print(f"Length is {index + 1}")
#             # a better way of the above code of getting the length of the index is:
#             # print(len(todos))
#
#         case 'complete':
#             number = int(input("Number of the todo to complete: "))
#
#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()
#
#             index = number - 1
#             todo_to_remove = todos[index].strip('\n')
#             todos.pop(index)  # negative 1 because in the case edit we had a negative 1
#
#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#             message = f"Todo {todo_to_remove} was removed from the list"
#             print(message)
#         case 'edit':
#             number = int(input("Number of the todo to edit: "))
#             number = number - 1  # we use -1 to start the index at 0 as the user will not know pythin starts at 0
#
#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()
#             print('Here is the existing list: ', todos)
#
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo + '\n'
#
#             print('Here is the modified list: ', todos)
#
#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#         case 'exit':
#             break
#         case anyvariable:  #on-demand variable. case _: is conventional
#             print("Please enter one of the menu command")
#
#
# print(("Bye!"))


# # Day 9 if else, list slicing
#
# todos = []
#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
#
#     if 'add' in user_action or 'new' in user_action:
#         todo = user_action[4:]
#
#         # the open and close code below can be more efficient
#         # using the 'with' function
#
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close() # should close always as a good coding practice
#
#         #  with - no need to close file as it will do it automatically
#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()
#
#
#         todos.append(todo)
#
#         # will replace the codes below with the with function to open file and automatically close file
#
#         # file = open('todos.txt', 'w') # create a todos.txt file in the same directory as the main.py first
#         # file.writelines(todos)
#         # file.close()  # should always good as coding practice
#
#         with open('todos.txt', 'w') as file:
#             file.writelines(todos)
#     elif 'show' in user_action:
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close()
#
#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()
#
#
#         # # 1st option - learning how to remove the '\n' so when we print it doesn't double-space
#         # new_todos = []
#         # for item in todos:
#         #     new_item = item.strip('\n')
#         #     new_todos.append(new_item)
#
#         # 2nd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#         # List Comprehension
#         new_todos = [item.strip('\n') for item in todos]
#
#         # for index, item in enumerate(todos):
#         for index, item in enumerate(new_todos):
#             item = item.title()
#
#             # # 3rd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#             item = item.strip('\n')
#
#             # index = index + 1 add the + 1 in the f string
#             # print(index, '-', items) # this will have a space like this '1 - Hey', but we want '1-Hey' with no spaces between the dash
#
#             row = f"{index + 1}-{item}"  #call f"" string. index + 1 so that the index starts 1, 2, 3... instead of 0, 1, 2...
#             print(row)
#
#         #print("Hello", index, item) -- once the program shows the items it will print Hello, the number of the last index and display the last item in the list as it exit out the loop
#         # print("Length is  ", index)
#         # print(f"Length is {index + 1}")
#         # a better way of the above code of getting the length of the index is:
#         # print(len(todos))
#
#     elif 'complete' in user_action:
#         number = int(user_action[9:])
#
#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()
#
#         index = number - 1
#         todo_to_remove = todos[index].strip('\n')
#         todos.pop(index)  # negative 1 because in the case edit we had a negative 1
#
#         with open('todos.txt', 'w') as file:
#             file.writelines(todos)
#         message = f"Todo {todo_to_remove} was removed from the list"
#         print(message)
#     elif 'edit' in user_action:
#         number = int(user_action[5:])
#         number = number - 1  # we use -1 to start the index at 0 as the user will not know pythin starts at 0
#
#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()
#         print('Here is the existing list: ', todos)
#
#         new_todo = input("Enter new todo: ")
#         todos[number] = new_todo + '\n'
#
#         print('Here is the modified list: ', todos)
#
#         with open('todos.txt', 'w') as file:
#             file.writelines(todos)
#     elif 'exit' in user_action:
#         break
#     else:
#         print("Command is not valid.")
#
#
# print(("Bye!"))


# # Day 10 We got bugs, try except
# # Syntax errors and exceptions
#
# todos = []
#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
#
#     if user_action.startswith('add') or user_action.startswith('new'):
#         todo = user_action[4:]
#
#         # the open and close code below can be more efficient
#         # using the 'with' function
#
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close() # should close always as a good coding practice
#
#         #  with - no need to close file as it will do it automatically
#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()
#
#
#         todos.append(todo + '\n')
#
#         # will replace the codes below with the with function to open file and automatically close file
#
#         # file = open('todos.txt', 'w') # create a todos.txt file in the same directory as the main.py first
#         # file.writelines(todos)
#         # file.close()  # should always good as coding practice
#
#         with open('todos.txt', 'w') as file:
#             file.writelines(todos)
#     elif user_action.startswith('show') or user_action.startswith('display'):
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close()
#
#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()
#
#
#         # # 1st option - learning how to remove the '\n' so when we print it doesn't double-space
#         # new_todos = []
#         # for item in todos:
#         #     new_item = item.strip('\n')
#         #     new_todos.append(new_item)
#
#         # 2nd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#         # List Comprehension
#         new_todos = [item.strip('\n') for item in todos]
#
#         # for index, item in enumerate(todos):
#         for index, item in enumerate(new_todos):
#             item = item.title()
#
#             # # 3rd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#             item = item.strip('\n')
#
#             # index = index + 1 add the + 1 in the f string
#             # print(index, '-', items) # this will have a space like this '1 - Hey', but we want '1-Hey' with no spaces between the dash
#
#             row = f"{index + 1}-{item}"  #call f"" string. index + 1 so that the index starts 1, 2, 3... instead of 0, 1, 2...
#             print(row)
#
#         #print("Hello", index, item) -- once the program shows the items it will print Hello, the number of the last index and display the last item in the list as it exit out the loop
#         # print("Length is  ", index)
#         # print(f"Length is {index + 1}")
#         # a better way of the above code of getting the length of the index is:
#         # print(len(todos))
#
#     elif user_action.startswith('complete'):
#         try:
#             number = int(user_action[9:])
#
#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()
#
#             index = number - 1
#             todo_to_remove = todos[index].strip('\n')
#             todos.pop(index)  # negative 1 because in the case edit we had a negative 1
#
#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#             message = f"Todo {todo_to_remove} was removed from the list"
#             print(message)
#         except IndexError:
#             print("There is no item with tha number.")
#             continue
#
#     elif user_action.startswith('edit'):
#         try:
#             number = int(user_action[5:])
#             number = number - 1  # we use -1 to start the index at 0 as the user will not know pythin starts at 0
#
#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()
#             print('Here is the existing list: ', todos)
#
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo + '\n'
#
#             print('Here is the modified list: ', todos)
#
#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#         except ValueError:
#             print("Your command is not valid.")
#             # user_action = input("Type add, show, edit, complete or exit: ")
#             # user_action = user_action.strip()
#             continue # continue will break and re-run the program from the start
#
#     elif user_action.startswith('exit'):
#         break
#     else:
#         print("Command is not valid.")
#
# print(("Bye!"))


# # Day 10 We got bugs, try except
# # Syntax errors and exceptions
#
# todos = []
#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
#
#     if user_action.startswith('add') or user_action.startswith('new'):
#         todo = user_action[4:]
#
#         # the open and close code below can be more efficient
#         # using the 'with' function
#
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close() # should close always as a good coding practice
#
#         #  with - no need to close file as it will do it automatically
#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()
#
#
#         todos.append(todo + '\n')
#
#         # will replace the codes below with the with function to open file and automatically close file
#
#         # file = open('todos.txt', 'w') # create a todos.txt file in the same directory as the main.py first
#         # file.writelines(todos)
#         # file.close()  # should always good as coding practice
#
#         with open('todos.txt', 'w') as file:
#             file.writelines(todos)
#     elif user_action.startswith('show') or user_action.startswith('display'):
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close()
#
#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()
#
#
#         # # 1st option - learning how to remove the '\n' so when we print it doesn't double-space
#         # new_todos = []
#         # for item in todos:
#         #     new_item = item.strip('\n')
#         #     new_todos.append(new_item)
#
#         # 2nd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#         # List Comprehension
#         new_todos = [item.strip('\n') for item in todos]
#
#         # for index, item in enumerate(todos):
#         for index, item in enumerate(new_todos):
#             item = item.title()
#
#             # # 3rd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#             item = item.strip('\n')
#
#             # index = index + 1 add the + 1 in the f string
#             # print(index, '-', items) # this will have a space like this '1 - Hey', but we want '1-Hey' with no spaces between the dash
#
#             row = f"{index + 1}-{item}"  #call f"" string. index + 1 so that the index starts 1, 2, 3... instead of 0, 1, 2...
#             print(row)
#
#         #print("Hello", index, item) -- once the program shows the items it will print Hello, the number of the last index and display the last item in the list as it exit out the loop
#         # print("Length is  ", index)
#         # print(f"Length is {index + 1}")
#         # a better way of the above code of getting the length of the index is:
#         # print(len(todos))
#
#     elif user_action.startswith('complete'):
#         try:
#             number = int(user_action[9:])
#
#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()
#
#             index = number - 1
#             todo_to_remove = todos[index].strip('\n')
#             todos.pop(index)  # negative 1 because in the case edit we had a negative 1
#
#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#             message = f"Todo {todo_to_remove} was removed from the list"
#             print(message)
#         except IndexError:
#             print("There is no item with tha number.")
#             continue
#
#     elif user_action.startswith('edit'):
#         try:
#             number = int(user_action[5:])
#             number = number - 1  # we use -1 to start the index at 0 as the user will not know pythin starts at 0
#
#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()
#             print('Here is the existing list: ', todos)
#
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo + '\n'
#
#             print('Here is the modified list: ', todos)
#
#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#         except ValueError:
#             print("Your command is not valid.")
#             # user_action = input("Type add, show, edit, complete or exit: ")
#             # user_action = user_action.strip()
#             continue # continue will break and re-run the program from the start
#
#     elif user_action.startswith('exit'):
#         break
#     else:
#         print("Command is not valid.")
#
# print(("Bye!"))


# # Day 11 Custom function
# # Code has redundancy - avoid this by custom function
#
# # todos = []
#
#
# def get_todos():
#     with open('todos.txt', 'r') as file:
#         todos_local = file.readlines()
#     return todos_local
# # function is recommended to have two spaces
# # function is recommended to have two spaces
#
#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
#
#     if user_action.startswith('add') or user_action.startswith('new'):
#         todo = user_action[4:]
#
#         # the open and close code below can be more efficient
#         # using the 'with' function
#
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close() # should close always as a good coding practice
#
#         #  with - no need to close file as it will do it automatically
#         # with open('todos.txt', 'r') as file:
#         #     todos = file.readlines()
#
#         todos = get_todos()
#
#         todos.append(todo + '\n')
#
#         # will replace the codes below with the with function to open file and automatically close file
#
#         # file = open('todos.txt', 'w') # create a todos.txt file in the same directory as the main.py first
#         # file.writelines(todos)
#         # file.close()  # should always good as coding practice
#
#         with open('todos.txt', 'w') as file:
#             file.writelines(todos)
#     elif user_action.startswith('show') or user_action.startswith('display'):
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close()
#
#         # with open('todos.txt', 'r') as file:
#         #     todos = file.readlines()
#
#         todos = get_todos()
#
#         # # 1st option - learning how to remove the '\n' so when we print it doesn't double-space
#         # new_todos = []
#         # for item in todos:
#         #     new_item = item.strip('\n')
#         #     new_todos.append(new_item)
#
#         # 2nd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#         # List Comprehension
#         new_todos = [item.strip('\n') for item in todos]
#
#         # for index, item in enumerate(todos):
#         for index, item in enumerate(new_todos):
#             item = item.title()
#
#             # # 3rd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#             item = item.strip('\n')
#
#             # index = index + 1 add the + 1 in the f string
#             # print(index, '-', items) # this will have a space like this '1 - Hey', but we want '1-Hey' with no spaces between the dash
#
#             row = f"{index + 1}-{item}"  #call f"" string. index + 1 so that the index starts 1, 2, 3... instead of 0, 1, 2...
#             print(row)
#
#         #print("Hello", index, item) -- once the program shows the items it will print Hello, the number of the last index and display the last item in the list as it exit out the loop
#         # print("Length is  ", index)
#         # print(f"Length is {index + 1}")
#         # a better way of the above code of getting the length of the index is:
#         # print(len(todos))
#
#     elif user_action.startswith('complete'):
#         try:
#             number = int(user_action[9:])
#
#             # with open('todos.txt', 'r') as file:
#             #     todos = file.readlines()
#
#             todos = get_todos()
#
#             index = number - 1
#             todo_to_remove = todos[index].strip('\n')
#             todos.pop(index)  # negative 1 because in the case edit we had a negative 1
#
#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#             message = f"Todo {todo_to_remove} was removed from the list"
#             print(message)
#         except IndexError:
#             print("There is no item with tha number.")
#             continue
#
#     elif user_action.startswith('edit'):
#         try:
#             number = int(user_action[5:])
#             number = number - 1  # we use -1 to start the index at 0 as the user will not know pythin starts at 0
#
#             # with open('todos.txt', 'r') as file:
#             #     todos = file.readlines()
#
#             todos = get_todos()
#
#             print('Here is the existing list: ', todos)
#
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo + '\n'
#
#             print('Here is the modified list: ', todos)
#
#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#         except ValueError:
#             print("Your command is not valid.")
#             # user_action = input("Type add, show, edit, complete or exit: ")
#             # user_action = user_action.strip()
#             continue # continue will break and re-run the program from the start
#
#     elif user_action.startswith('exit'):
#         break
#     else:
#         print("Command is not valid.")
#
# print("Bye!")


# # Day 12 Custom Functions
#
# # todos = []
#
#
# def get_todos(filepath):
#     with open(filepath, 'r') as file:
#         todos_local = file.readlines()
#     return todos_local
# # function is recommended to have two spaces
# # function is recommended to have two spaces
#
#
# def write_todos(filepath, todos_arg):
#     with open(filepath, 'w') as file:
#         file.writelines(todos_arg)
#     # no return because the write method modifies and does not need to return
#
#
#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
#
#     if user_action.startswith('add') or user_action.startswith('new'):
#         todo = user_action[4:]
#
#         # the open and close code below can be more efficient
#         # using the 'with' function
#
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close() # should close always as a good coding practice
#
#         #  with - no need to close file as it will do it automatically
#         # with open('todos.txt', 'r') as file:
#         #     todos = file.readlines()
#
#         todos = get_todos('todos.txt')
#
#         todos.append(todo + '\n')
#
#         # will replace the codes below with the with function to open file and automatically close file
#
#         # file = open('todos.txt', 'w') # create a todos.txt file in the same directory as the main.py first
#         # file.writelines(todos)
#         # file.close()  # should always good as coding practice
#
#         # with open('todos.txt', 'w') as file:
#         #     file.writelines(todos)
#
#         write_todos('todos.txt', todos)  # since write doesn't return anything we don't need to assigned it to a variable
#
#
#     elif user_action.startswith('show') or user_action.startswith('display'):
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close()
#
#         # with open('todos.txt', 'r') as file:
#         #     todos = file.readlines()
#
#         todos = get_todos('todos.txt')
#
#         # # 1st option - learning how to remove the '\n' so when we print it doesn't double-space
#         # new_todos = []
#         # for item in todos:
#         #     new_item = item.strip('\n')
#         #     new_todos.append(new_item)
#
#         # 2nd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#         # List Comprehension
#         new_todos = [item.strip('\n') for item in todos]
#
#         # for index, item in enumerate(todos):
#         for index, item in enumerate(new_todos):
#             item = item.title()
#
#             # # 3rd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#             item = item.strip('\n')
#
#             # index = index + 1 add the + 1 in the f string
#             # print(index, '-', items) # this will have a space like this '1 - Hey', but we want '1-Hey' with no spaces between the dash
#
#             row = f"{index + 1}-{item}"  #call f"" string. index + 1 so that the index starts 1, 2, 3... instead of 0, 1, 2...
#             print(row)
#
#         #print("Hello", index, item) -- once the program shows the items it will print Hello, the number of the last index and display the last item in the list as it exit out the loop
#         # print("Length is  ", index)
#         # print(f"Length is {index + 1}")
#         # a better way of the above code of getting the length of the index is:
#         # print(len(todos))
#
#     elif user_action.startswith('complete'):
#         try:
#             number = int(user_action[9:])
#
#             # with open('todos.txt', 'r') as file:
#             #     todos = file.readlines()
#
#             todos = get_todos('todos.txt')
#
#             index = number - 1
#             todo_to_remove = todos[index].strip('\n')
#             todos.pop(index)  # negative 1 because in the case edit we had a negative 1
#
#             # with open('todos.txt', 'w') as file:
#             #     file.writelines(todos)
#
#             write_todos('todos.txt', todos)
#
#             message = f"Todo {todo_to_remove} was removed from the list"
#             print(message)
#
#         except IndexError:
#             print("There is no item with tha number.")
#             continue
#
#     elif user_action.startswith('edit'):
#         try:
#             number = int(user_action[5:])
#             number = number - 1  # we use -1 to start the index at 0 as the user will not know pythin starts at 0
#
#             # with open('todos.txt', 'r') as file:
#             #     todos = file.readlines()
#
#             todos = get_todos('todos.txt')
#
#             print('Here is the existing list: ', todos)
#
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo + '\n'
#
#             print('Here is the modified list: ', todos)
#
#             # with open('todos.txt', 'w') as file:
#             #     file.writelines(todos)
#
#             write_todos('todos.txt', todos)
#
#         except ValueError:
#             print("Your command is not valid.")
#             # user_action = input("Type add, show, edit, complete or exit: ")
#             # user_action = user_action.strip()
#             continue # continue will break and re-run the program from the start
#
#     elif user_action.startswith('exit'):
#         break
#     else:
#         print("Command is not valid.")
#
# print("Bye!")


# # Day 13 Default params & Doc strings
#
# # todos = []
#
#
# def get_todos(filepath="todos.txt"):
#     """
#         Read a text file and return the list of
#         todos items
#     """
#     with open(filepath, 'r') as file:
#         todos_local = file.readlines()
#     return todos_local
# # function is recommended to have two spaces
# # function is recommended to have two spaces
#
#
# # print(help(get_todos))  # This prints out the doc strings
#
#
# def write_todos(todos_arg=todos, filepath="todos.txt"):  # default param are at the end
#     """ Write the to-do items list in the text file."""
#     with open(filepath, 'w') as file:
#         file.writelines(todos_arg)
#     # no return because the write method modifies and does not need to return
#
#
# text = """
# Principles of productivity:
# Managing your inflow.
# Systemizing everything that repeats.
# """
#
# print(text)
#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
#
#     if user_action.startswith('add') or user_action.startswith('new'):
#         todo = user_action[4:]
#
#         # the open and close code below can be more efficient
#         # using the 'with' function
#
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close() # should close always as a good coding practice
#
#         #  with - no need to close file as it will do it automatically
#         # with open('todos.txt', 'r') as file:
#         #     todos = file.readlines()
#
#         # todos = get_todos('todos.txt')
#         todos = get_todos()  # Using default params
#
#         todos.append(todo + '\n')
#
#         # will replace the codes below with the with function to open file and automatically close file
#
#         # file = open('todos.txt', 'w') # create a todos.txt file in the same directory as the main.py first
#         # file.writelines(todos)
#         # file.close()  # should always good as coding practice
#
#         # with open('todos.txt', 'w') as file:
#         #     file.writelines(todos)
#
#         # write_todos('todos.txt', todos)  # since write doesn't return anything we don't need to assigned it to a variable
#         write_todos(todos)  # Using default param
#
#
#     elif user_action.startswith('show') or user_action.startswith('display'):
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close()
#
#         # with open('todos.txt', 'r') as file:
#         #     todos = file.readlines()
#
#         # todos = get_todos('todos.txt')
#         todos = get_todos()  # Using default params
#
#         # # 1st option - learning how to remove the '\n' so when we print it doesn't double-space
#         # new_todos = []
#         # for item in todos:
#         #     new_item = item.strip('\n')
#         #     new_todos.append(new_item)
#
#         # 2nd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#         # List Comprehension
#         new_todos = [item.strip('\n') for item in todos]
#
#         # for index, item in enumerate(todos):
#         for index, item in enumerate(new_todos):
#             item = item.title()
#
#             # # 3rd option - inline for loop to remove the '\n' so when we print it doesn't double-space
#             item = item.strip('\n')
#
#             # index = index + 1 add the + 1 in the f string
#             # print(index, '-', items) # this will have a space like this '1 - Hey', but we want '1-Hey' with no spaces between the dash
#
#             row = f"{index + 1}-{item}"  #call f"" string. index + 1 so that the index starts 1, 2, 3... instead of 0, 1, 2...
#             print(row)
#
#         #print("Hello", index, item) -- once the program shows the items it will print Hello, the number of the last index and display the last item in the list as it exit out the loop
#         # print("Length is  ", index)
#         # print(f"Length is {index + 1}")
#         # a better way of the above code of getting the length of the index is:
#         # print(len(todos))
#
#     elif user_action.startswith('complete'):
#         try:
#             number = int(user_action[9:])
#
#             # with open('todos.txt', 'r') as file:
#             #     todos = file.readlines()
#
#             # todos = get_todos('todos.txt')
#             todos = get_todos()  # Using default params
#
#             index = number - 1
#             todo_to_remove = todos[index].strip('\n')
#             todos.pop(index)  # negative 1 because in the case edit we had a negative 1
#
#             # with open('todos.txt', 'w') as file:
#             #     file.writelines(todos)
#
#             # write_todos('todos.txt', todos)
#             write_todos( todos)  # Using default param
#
#             message = f"Todo {todo_to_remove} was removed from the list"
#             print(message)
#
#         except IndexError:
#             print("There is no item with tha number.")
#             continue
#
#     elif user_action.startswith('edit'):
#         try:
#             number = int(user_action[5:])
#             number = number - 1  # we use -1 to start the index at 0 as the user will not know pythin starts at 0
#
#             # with open('todos.txt', 'r') as file:
#             #     todos = file.readlines()
#
#             # todos = get_todos('todos.txt')
#             todos = get_todos()  # Using default params
#
#             print('Here is the existing list: ', todos)
#
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo + '\n'
#
#             print('Here is the modified list: ', todos)
#
#             # with open('todos.txt', 'w') as file:
#             #     file.writelines(todos)
#
#             # write_todos('todos.txt', todos)
#             write_todos( todos)  # Using default param
#
#         except ValueError:
#             print("Your command is not valid.")
#             # user_action = input("Type add, show, edit, complete or exit: ")
#             # user_action = user_action.strip()
#             continue # continue will break and re-run the program from the start
#
#     elif user_action.startswith('exit'):
#         break
#     else:
#         print("Command is not valid.")
#
# print("Bye!")


# # Day 14 We will separate the functions to another file
#
# # todos = []
#
# # from functions import get_todos, write_todos
# from modules import functions
#
# text = """
# Principles of productivity:
# Managing your inflow.
# Systemizing everything that repeats.
# """
#
# print(text)
#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
#
#     if user_action.startswith('add') or user_action.startswith('new'):
#         todo = user_action[4:]
#
#         todos = functions.get_todos()  # Using default params
#
#         todos.append(todo + '\n')
#
#         functions.write_todos(todos)  # Using default param
#
#     elif user_action.startswith('show') or user_action.startswith('display'):
#
#         todos = functions.get_todos()  # Using default params
#
#         new_todos = [item.strip('\n') for item in todos]
#         for index, item in enumerate(new_todos):
#             item = item.title()
#
#             item = item.strip('\n')
#
#             row = f"{index + 1}-{item}"  # call f"" string. index + 1 so that the index starts 1, 2, 3... instead of 0, 1, 2...
#             print(row)
#
#     elif user_action.startswith('complete'):
#         try:
#             number = int(user_action[9:])
#
#             todos = functions.get_todos()  # Using default params
#
#             index = number - 1
#             todo_to_remove = todos[index].strip('\n')
#             todos.pop(index)  # negative 1 because in the case edit we had a negative 1
#
#             functions.write_todos(todos)  # Using default param
#
#             message = f"Todo {todo_to_remove} was removed from the list"
#             print(message)
#
#         except IndexError:
#             print("There is no item with tha number.")
#             continue
#
#     elif user_action.startswith('edit'):
#         try:
#             number = int(user_action[5:])
#             number = number - 1  # we use -1 to start the index at 0 as the user will not know pythin starts at 0
#
#             todos = functions.get_todos()  # Using default params
#
#             print('Here is the existing list: ', todos)
#
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo + '\n'
#
#             print('Here is the modified list: ', todos)
#
#             functions.write_todos(todos)  # Using default param
#
#         except ValueError:
#             print("Your command is not valid.")
#
#             continue  # continue will break and re-run the program from the start
#
#     elif user_action.startswith('exit'):
#         break
#     else:
#         print("Command is not valid.")
#
# print("Bye!")


# # Day 15 Standard modules
#
# # todos = []
#
# # from functions import get_todos, write_todos
# from modules import functions
# import time
#
# now = time.strftime("%b %d, %Y %H:%M:%S")
#
# print("It is:",now)
#
# text = """
# Principles of productivity:
# Managing your inflow.
# Systemizing everything that repeats.
# """
#
# print(text)
#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
#
#     if user_action.startswith('add') or user_action.startswith('new'):
#         todo = user_action[4:]
#
#         todos = functions.get_todos()  # Using default params
#
#         todos.append(todo + '\n')
#
#         functions.write_todos(todos)  # Using default param
#
#     elif user_action.startswith('show') or user_action.startswith('display'):
#
#         todos = functions.get_todos()  # Using default params
#
#         new_todos = [item.strip('\n') for item in todos]
#         for index, item in enumerate(new_todos):
#             item = item.title()
#
#             item = item.strip('\n')
#
#             row = f"{index + 1}-{item}"  # call f"" string. index + 1 so that the index starts 1, 2, 3... instead of 0, 1, 2...
#             print(row)
#
#     elif user_action.startswith('complete'):
#         try:
#             number = int(user_action[9:])
#
#             todos = functions.get_todos()  # Using default params
#
#             index = number - 1
#             todo_to_remove = todos[index].strip('\n')
#             todos.pop(index)  # negative 1 because in the case edit we had a negative 1
#
#             functions.write_todos(todos)  # Using default param
#
#             message = f"Todo {todo_to_remove} was removed from the list"
#             print(message)
#
#         except IndexError:
#             print("There is no item with tha number.")
#             continue
#
#     elif user_action.startswith('edit'):
#         try:
#             number = int(user_action[5:])
#             number = number - 1  # we use -1 to start the index at 0 as the user will not know pythin starts at 0
#
#             todos = functions.get_todos()  # Using default params
#
#             print('Here is the existing list: ', todos)
#
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo + '\n'
#
#             print('Here is the modified list: ', todos)
#
#             functions.write_todos(todos)  # Using default param
#
#         except ValueError:
#             print("Your command is not valid.")
#
#             continue  # continue will break and re-run the program from the start
#
#     elif user_action.startswith('exit'):
#         break
#     else:
#         print("Command is not valid.")
#
# print("Bye!")


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