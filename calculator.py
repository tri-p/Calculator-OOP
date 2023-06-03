# PABUNA KATRINA B. 

# create class Calculator
class Calculator:

    # def add
    def add(self, num1, num2):
        sum = num1 + num2
        return

    # def subtract
    def sub(self):
        # ask for inputs
        try:
            num1 = float(input("\n\033[96m\033[1mInput the first number: \033[0m"))
            num2 = float(input("\033[96m\033[1mInput the second number: \033[0m"))
        except ValueError:
            print("\n\033[91mSyntax Error: Invalid input\033[97m\n")
            print("\033[93m=" * 80, "\n")
            exit()
        # get the difference of the two inputs
        diff = num1 - num2
        print("\n\033[92m" + str(num1), "-", str(num2) + 
            "\n\033[96m\033[1mDifference: \033[0m" + str(diff))
        Calculator.retry(self)
        return

    # def multiply
    def mul(self):
        # ask for inputs
        try:
            num1 = float(input("\n\033[96m\033[1mInput the first number: \033[0m"))
            num2 = float(input("\033[96m\033[1mInput the second number: \033[0m"))
        except ValueError:
            print("\n\033[91mSyntax Error: Invalid input\033[97m\n")
            print("\033[93m=" * 80, "\n")
            exit()
        # get the product of the two inputs
        prod = num1 * num2
        print("\n\033[92m" + str(num1), "*", str(num2) + 
            "\n\033[96m\033[1mProduct: \033[0m" + str(prod))
        Calculator.retry(self)
        return

    # def division
    def div(self):
        # ask for inputs
        try:
            num1 = float(input("\n\033[96m\033[1mInput the first number: \033[0m"))
            num2 = float(input("\033[96m\033[1mInput the second number: \033[0m"))
            # get the quotient of the two inputs
            quot = num1 / num2
        except ValueError:
            print("\n\033[91mSyntax Error: Invalid input\033[97m\n")
            print("\033[93m=" * 80, "\n")
            exit()
        except ZeroDivisionError:
            print("\n\033[91mMath Error: Division by zero\033[97m\n")
            print("\033[93m=" * 80, "\n")
            exit()
        print("\n\033[92m" + str(num1), "/", str(num2) + 
            "\n\033[96m\033[1mQuotient: \033[0m" + str(quot))
        Calculator.retry(self)
        return

    # def retry
    def retry(self):
        '''Create def retry where it asks the user if they would
        like to try again or not.''' 
        user_input = input("\n\033[95m\x1B[3m\033[1mWould you like to try again?\033[0m\n" +
                        "\033[92my \033[97m- Yes\n" +
                        "\033[92mn \033[97m- No\n\n" +
                        "\033[95m")
        if user_input.lower() == "y":
            Calculator.ask_operation(self)
        elif user_input.lower() == "n":
            print("\n\033[96m\x1B[3m\033[1mThank you!\033[0m")
            print("\n" + "\033[93m=" * 80 + "\n")
            exit()
        else:
            print("\n\033[91mError. Invalid input.\033[97m\n")
            print("\033[93m=" * 80 + "\n")
            exit()
        Calculator.retry(self)
        return