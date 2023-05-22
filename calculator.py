# PABUNA KATRINA B. 

# create class Calculator
class Calculator:

    # def ask_operation
    def ask_operation(self):
        '''Create def ask_operation where it lets the user to pick among
        addition, subtraction, multiplication, and division.'''
        user_input = input("\nWhat operation do you want to use?\n" +
                            "a - Add\n" +
                            "s - Subtract\n" +
                            "m - Multiply\n" +
                            "d - Divide\n\n")
        if user_input.lower() == "a":
            Calculator.add(self) # should lead to add function
        elif user_input.lower() == "s":
            Calculator.sub(self) # should lead to sub function
        elif user_input.lower() == "m":
            Calculator.mul(self) # should lead to mul function
        elif user_input.lower() == "d":
            Calculator.div(self) # should lead to div function
        else:
            print("Error. Invalid input.")
            exit()
        return

    # def add
    def add(self):
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
        Calculator.retry(self)
        return

    # def subtract
    def sub(self):
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
        Calculator.retry(self)
        return

    # def multiply
    def mul(self):
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
        Calculator.retry(self)
        return

    # def division
    def div(self):
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
        Calculator.retry(self)
        return

    # def retry
    def retry(self):
        '''Create def retry where it asks the user if they would
        like to try again or not.''' 
        user_input = input("\nWould you like to try again?\n" +
                        "y - Yes\n" +
                        "n - No\n\n")
        if user_input.lower() == "y":
            Calculator.ask_operation(self)
        elif user_input.lower() == "n":
            print("Thank you!")
            exit()
        else:
            print("Error. Invalid input.")
            exit()
        Calculator.retry(self)
        return