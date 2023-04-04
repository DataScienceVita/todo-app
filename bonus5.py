waiting_list = ["sen", "ben", "john"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)

filenames = ['document', 'report', 'presentation']
for i, j in enumerate(filenames):
    print(f'{i}-{j.capitalize()}.txt')

ips = ['100.122.133.105', '100.122.133.111']

user_choice = int(input("Enter the index of the IP you want: "))
message = f"You chose {ips[user_choice]}"
print(message)