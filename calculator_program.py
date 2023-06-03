# PABUNA, KATRINA B. 

# import class
from user_interface import UserInterface
from calculator import Calculator
from calc_operations import CalculatorOperations

ui = UserInterface()
calc = Calculator()
op = CalculatorOperations()

# ==== start ====
while True:
    # ask operation
    user_input = ui.ask_operation().lower()
    if user_input == "a":
        op.add_ans() # should lead to add function
    elif user_input == "s":
        op.sub_ans() # should lead to sub function
    elif user_input == "m": 
        op.mul_ans() # should lead to mul function
    elif user_input == "d": 
        op.div_ans() # should lead to div function
    else:
        print("\033[91mError. Invalid input.\033[97m")
        print("\n" + "\033[93m=" * 80 + "\n")
        exit()

    # retry
    if not ui.retry():
        print("\n\033[96m\x1B[3m\033[1mThank you!\033[0m")
        print("\n" + "\033[93m=" * 80 + "\n")
        break