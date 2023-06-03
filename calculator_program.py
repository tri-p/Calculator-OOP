# PABUNA, KATRINA B. 

# import class
from user_interface import UserInterface
from calculator import Calculator

ui = UserInterface()
calc = Calculator()

# ==== start ====
# ask operation
user_input = ui.ask_operation()
if user_input == "a":
    calc.add(num1, num2) # should lead to add function

# ask to input two numbers
num1 = ui.input_user()
num2 = ui.input_user()

# if the user enters "a"
sum = calc.add(num1, num2)
ui.print_sum(sum)

# if the user enters "s"
calc.sub()

# if the user enters "m"
calc.mul()

# if the user enters "d"
calc.div()

# prompts the user if they would like to try again
calc.retry()