"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    add_answer = num1 + num2
    #print(add_answer)
    
    return  add_answer


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    subtract_answer = num1 - num2
    #print(subtract_answer)

    return subtract_answer

def multiply(num1, num2):
    """Multiply the two inputs together."""
    mult_answer = num1 * num2
    #print(mult_answer)

    return mult_answer

def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    divide_answer = num1 / num2
    #print(divide_answer)

    return divide_answer

def square(num1):
    """Return the square of the input."""
    square_answer = num1 ** 2
    #print(square_answer)

    return square_answer



def cube(num1):
    """Return the cube of the input."""
    cube_answer = num1 ** 3
    #print(cube_answer)

    return cube_answer

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    power_answer = num1 ** num2
    #print(power_answer)

    return power_answer


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    mod_answer = num1 % num2
    #print(mod_answer)

    return mod_answer
