
# Concepts of decoupling


# feet_inches = input("Enter feet and inches: ")
#
#
# def convert(feet_inches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#
#     meters = (feet * 0.3048) + (inches * 0.0254)
#     # return f"{feet} and {inches} inches is equals to {meters} meters."
#     # The code above is our original code but the idea of decoupling is to "Return" a single value instead of an f string
#
#     return meters
#
#
# result = (convert(feet_inches))
#
# if result < 1:
#     print("Kid is too small.")
# else:
#     print("Kid can use the slide")


# So the function above from Day 12 is doing too much. Function should have one job and do it well
# Out function below was taking input and parsing and then extracting numbers... etc
# So decoupling by creating more functions for each function task



feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    # return feet, inches
    return {"feet": feet, "inches": inches}

def convert(feet, inches):
    meters = (feet * 0.3048) + (inches * 0.0254)
    # return f"{feet} and {inches} inches is equals to {meters} meters."
    # The code above is our original code but the idea of decoupling is to "Return" a single value instead of an f string
    return meters


parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])


print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")  # we use a single quote for the dictionary key because we already have a double quote from the f strong

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide")

