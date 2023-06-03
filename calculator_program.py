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
    user_input = ui.ask_operation()
    if user_input == "a":
        add_ans # should lead to add function
    elif user_input == "s":
        calc.sub() # should lead to sub function
    elif user_input == "m": 
        calc.mul() # should lead to mul function
    elif user_input == "d":
        calc.div() # should lead to div function
    else:
        print("\n\033[91mError. Invalid input.\033[97m\n")
        exit()

    # ask to input two numbers
    num1 = ui.input_user()
    num2 = ui.input_user()

    # if the user enters "a" - add
    def add_ans(self):
        sum = calc.add(num1, num2)
        ui.print_sum(sum)

    # if the user enters "s" - subtract
    diff = calc.sub(num1, num2)
    ui.print_diff(diff)

    # if the user enters "m" - multiply
    prod = calc.mul(num1, num2)
    ui.print_prod(prod)

    # if the user enters "d" - divide
    quot = calc.div(num1, num2)
    ui.print_quot(quot)

    # retry
    if not ui.retry():
        print("\n\033[96m\x1B[3m\033[1mThank you!\033[0m")
        print("\n" + "\033[93m=" * 80 + "\n")
        break