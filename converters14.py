def convert(feet, inches):
    meters = (feet * 0.3048) + (inches * 0.0254)
    # return f"{feet} and {inches} inches is equals to {meters} meters."
    # The code above is our original code but the idea of decoupling is to "Return" a single value instead of an f string
    return meters
