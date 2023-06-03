# PABUNA KATRINA B. 

# create class Calculator
class Calculator:

    # def add
    def add(self, num1, num2):
        sum = num1 + num2
        return sum

    # def subtract
    def sub(self, num1, num2):
        diff = num1 - num2
        return diff

    # def multiply
    def mul(self, num1, num2):
        prod = num1 * num2
        return prod

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
        return