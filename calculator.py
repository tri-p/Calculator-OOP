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
        print("Syntax Error: Invalid input")
    # get the sum of the two inputs
    sum = num1 + num2
    print(str(num1), "+", str(num2) + 
        "\nSum: " + str(sum))
    retry()

# def subtract
def sub():
    # ask for inputs
    try:
        num1 = float(input("\nInput the first number: "))
        num2 = float(input("Input the second number: "))
    except ValueError:
        print("Syntax Error: Invalid input")
    # get the difference of the two inputs
    diff = num1 - num2
    print(str(num1), "-", str(num2) + 
        "\nDifference: " + str(diff))
    retry()

# def multiply
def mul():
    # ask for inputs
    try:
        num1 = float(input("\nInput the first number: "))
        num2 = float(input("Input the second number: "))
    except ValueError:
        print("Syntax Error: Invalid input")
    # get the product of the two inputs
    prod = num1 * num2
    print(str(num1), "*", str(num2) + 
        "\nProduct: " + str(prod))
    retry()

# def division
def div():
    # ask for inputs
    try:
        num1 = float(input("\nInput the first number: "))
        num2 = float(input("Input the second number: "))
    except ValueError:
        print("Syntax Error: Invalid input")
    except ZeroDivisionError:
        print("Math Error: Division by zero")
    # get the quotient of the two inputs
    quot = num1 / num2
    print(str(num1), "/", str(num2) + 
        "\nQuotient: " + str(quot))
    retry()

# def retry
def retry():
    '''Create def retry where it asks the user if they would
    like to try again or not.''' 
    user_input = input("\nWould you like to try again?\n" +
                    "y - Yes\n" +
                    "n - No\n\n")
    if user_input.lower() == "y":
        ask_operation()
    elif user_input.lower() == "n":
        print("Thank you!")
        exit()
    else:
        print("Error. Invalid input.")
    retry()

ask_operation()