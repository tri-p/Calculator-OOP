# PABUNA, KATRINA B. 

# import class
from calculator import Calculator

calc = Calculator()

# ==== start ====
# ask operation
calc.ask_operation()

# if the user enters "a"
calc.add()

# if the user enters "s"
calc.sub()

# if the user enters "m"
calc.mul()

# if the user enters "d"
calc.div()

# propts the user if they would like to try again
calc.retry()