# This function adds two numbers
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error: Denominator can't be zero."
    else:
        return result