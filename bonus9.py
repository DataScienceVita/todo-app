# Program to check password strength
# Dictionary


password = input("Enter a new password: ")

# result = [] # List
result = {} # {key:value, key:value}

if len(password) >= 8:
    # result.append(True)
    result["Length: "] = True
else:
    # result.append(False)
    result["Length: "] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["Digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["Uppercase"] = uppercase

print(result)
# print(all(result))

# if all(result) == True: is equal to if all(result):
if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")