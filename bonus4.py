filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentation.txt"]

# In this example we cannot use the trick we did below with the case edit because
# List[] can be mutable but our list above filenames = [... are strings and strings cannot be changed

# case
# 'edit':
# number = int(input("Number of the todo to edit: "))
# number = number - 1
# new_todo = input("Enter new todo: ")
# todos[number] = new_todo

# Test
# filename = "1.Raw Data.txt"
# filename[1] = "-"
# this will produce an error due to strings cannot be changed
# a workaround is to use the method .replace('.', '-')

# filename_new = filename.replace('.', '-')
# filename_new
# filename_new = filename.replace('.', '-', 1) the 1 means to change the first occurrence of the '.'

# Test
# todos = ["clean it", "throw it"]
# todos[1] = "get it"


for filename in filenames:
    print(filename)
    filename = filename.replace('.', '-', 1)
    print(filename)
