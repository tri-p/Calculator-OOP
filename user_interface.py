# PABUNA, KATRINA B. 

# create class UserInterface
class UserInterface:

    # def ask_operation
    def ask_operation(self):
        '''Create def ask_operation where it lets the user to pick among
        addition, subtraction, multiplication, and division.'''
        print("\n" + "\033[93m=" * 80 + "\n")
        user_input = input("\n\033[95m\x1B[3m\033[1mWhat operation do you want to use?\033[0m\n" +
                            "\033[92ma \033[97m- Add\n" +
                            "\033[92ms \033[97m- Subtract\n" +
                            "\033[92mm \033[97m- Multiply\n" +
                            "\033[92md \033[97m- Divide\n\n" +
                            "\033[95m")
        user_input = user_input.lower()
        print("\n")
        return

    # ask for inputs
    def input_user(self):
        try:
            number = input("\033[96m\033[1mInput a number: \033[0m")
            number = float(number)
            return number
        except ValueError:
            print("Input a number only.")
            return self.input_user()

    # print sum
    def print_sum(self, sum):
        print("\n\033[96m\033[1mSum: \033[0m" + str(sum))
        return