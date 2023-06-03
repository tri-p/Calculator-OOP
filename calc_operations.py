# PABUNA, KATRINA B. 

# import class
from user_interface import UserInterface
from calculator import Calculator

ui = UserInterface()
calc = Calculator()

class CalculatorOperations(UserInterface, Calculator):
    def add_ans(self):
        print("\n")
        num1 = ui.input_user()
        num2 = ui.input_user()
        sum = calc.add(num1, num2)
        ans = print("\n\033[92m" + str(num1) + " + " + str(num2)) 
        ui.print_sum(sum)
        return 