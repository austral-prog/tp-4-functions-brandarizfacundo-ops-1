# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    if x >= y :
        return "x"
    else:
        return"y"
    # Remove this line and implement


def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if x == y and y == z:
        return {x}
    elif x > y and x > z:
        return {x}
    elif y > x and y > z:
        return {y}
    elif z>x and z>y:
        return {z}

