# PABUNA, KATRINA B. 

# import class
from user_interface import UserInterface
from calculator import Calculator

ui = UserInterface()
calc = Calculator()

# ==== start ====
while True:
    # ask operation
    user_input = ui.ask_operation()
    if user_input == "a":
        calc.add(num1, num2) # should lead to add function
    elif user_input == "s":
        calc.sub(num1, num2) # should lead to sub function

    # ask to input two numbers
    num1 = ui.input_user()
    num2 = ui.input_user()

    # if the user enters "a" - add
    sum = calc.add(num1, num2)
    ui.print_sum(sum)

    # if the user enters "s" - subtract
    diff = calc.sub(num1, num2)
    ui.print_diff(diff)

    # retry
    if not ui.retry():
        print("\n\033[96m\x1B[3m\033[1mThank you!\033[0m")
        print("\n" + "\033[93m=" * 80 + "\n")
        break
