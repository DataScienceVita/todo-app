filenames = ["1.doc", "1.report", "1.presentation"]

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print(filenames)

#
# temperatures = [10, 12, 14]
#
# temperatures = [str(i) + '\n' for i in temperatures]
#
# file = open("file.txt", 'w')
# file.writelines(temperatures)
#
#
# numbers = [10.1, 12.3, 14.7]
# numbers = [int(item) for item in numbers]
# print(numbers)