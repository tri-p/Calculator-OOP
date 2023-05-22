# PABUNA KATRINA B. 

# create class Calculator
class Calculator:
    def __init__(self, add, sub, mul, div):
        self.add = add
        self.sub = sub 
        self.mul = mul
        self.div = div

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

# def multiply

# def division

# def ask_operation
def ask_operation():
    '''Create def ask_operation where it lets the user pick among
    addition, subtraction, multiplication, and division.'''
    user_input = input("\nWhat operation do you want to use?\n" +
                        "a - Add\n" +
                        "s - Subtract\n" +
                        "m - Multiply\n" +
                        "d - Divide\n\n")
    if user_input.lower() == "a":
        add()
    ask_operation()
                            
ask_operation()
# def retry