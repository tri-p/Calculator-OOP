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

# def division

# def retry 

ask_operation()