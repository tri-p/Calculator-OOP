# PABUNA KATRINA B. 

# create class Calculator
class Calculator:
    # constructor
    def __init__(self, add, sub, mul, div):
        # intance variables
        self.add = add
        self.sub = sub 
        self.mul = mul
        self.div = div

# def ask_operation
def ask_operation():
    '''Create def ask_operation where it lets the user to pick among
    addition, subtraction, multiplication, and division.'''
    user_input = input("\nWhat operation do you want to use?\n" +
                        "a - Add\n" +
                        "s - Subtract\n" +
                        "m - Multiply\n" +
                        "d - Divide\n\n")
    if user_input.lower() == "a":
        add() # should lead to add function
    elif user_input.lower() == "s":
        sub() # should lead to sub function
    elif user_input.lower() == "m":
        mul() # should lead to mul function
    elif user_input.lower() == "d":
        div() # should lead to div function
    else:
        print("Error. Invalid input.")

# def add
def add():
    # ask for inputs
    try:
        num1 = float(input("\nInput the first number: "))
        num2 = float(input("Input the second number: "))
    except ValueError:
        print("Input a number only.")
    # get the sum of the two inputs
    sum = num1 + num2
    print(str(num1), "+", str(num2) + 
        "\nSum: " + str(sum))


# def subtract
def sub():
    # ask for inputs
    try:
        num1 = float(input("\nInput the first number: "))
        num2 = float(input("Input the second number: "))
    except ValueError:
        print("Input a number only.")
    # get the difference of the two inputs
    diff = num1 - num2
    print(str(num1), "-", str(num2) + 
        "\nDifference: " + str(diff))

# def multiply
def mul():
    # ask for inputs
    try:
        num1 = float(input("\nInput the first number: "))
        num2 = float(input("Input the second number: "))
    except ValueError:
        print("Input a number only.")
    # get the product of the two inputs
    prod = num1 * num2
    print(str(num1), "*", str(num2) + 
        "\nProduct: " + str(prod))

# def division
def div():
    # ask for inputs
    try:
        num1 = float(input("\nInput the first number: "))
        num2 = float(input("Input the second number: "))
    except ValueError:
        print("Input a number only.")
    except ZeroDivisionError:
        print("Division by zero")
    # get the quotient of the two inputs
    quot = num1 / num2
    print(str(num1), "/", str(num2) + 
        "\nQuotient: " + str(quot))

# def retry 

ask_operation()