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

    # ask to input two numbers
    num1 = ui.input_user()
    num2 = ui.input_user()

    # if the user enters "a"
    sum = calc.add(num1, num2)
    ui.print_sum(sum)

    # retry
    if not ui.retry():
        print("\n\033[96m\x1B[3m\033[1mThank you!\033[0m")
        print("\n" + "\033[93m=" * 80 + "\n")
        break
