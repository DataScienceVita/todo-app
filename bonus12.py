
# Concepts of decoupling


feet_inches = input("Enter feet and inches: ")


def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = (feet * 0.3048) + (inches * 0.0254)
    # return f"{feet} and {inches} inches is equals to {meters} meters."
    # The code above is our original code but the idea of decoupling is to "Return" a single value instead of an f string

    return meters


result = (convert(feet_inches))

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide")
