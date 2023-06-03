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
    def div(self, num1, num2):
        try:
            quot = num1 / num2
        except ZeroDivisionError:
            print("\n\033[91mMath Error: Division by zero\033[97m\n")
            print("\033[93m=" * 80, "\n")
            exit()
        return quot