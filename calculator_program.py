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
    calc.add() # should lead to add function

# if the user enters "a"
calc.add()

# if the user enters "s"
calc.sub()

# if the user enters "m"
calc.mul()

# if the user enters "d"
calc.div()

# prompts the user if they would like to try again
calc.retry()