# the code below came from the refractor after we moved the parse function to the "parsers14 file"
from converters14 import convert
from parsers14 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])


print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")  # we use a single quote for the dictionary key because we already have a double quote from the f strong

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide")

