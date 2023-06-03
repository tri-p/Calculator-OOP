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
        return user_input

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
    
    # print diff
    def print_diff(self, diff):
        print("\n\033[96m\033[1mDifference: \033[0m" + str(diff))
        return
    
    # print prod
    def print_prod(self, prod):
        print("\n\033[96m\033[1mProduct: \033[0m" + str(prod))
        return
    
    # print quot
    def print_quot(self, quot):
        print("\n\033[96m\033[1mQuotient: \033[0m" + str(quot))
        return
    
    # retry
    def retry(self):
        inp_try = input("\n\033[95m\x1B[3m\033[1mWould you like to try again?\033[0m\n" +
                        "\033[92my \033[97m- Yes\n" +
                        "\033[92mn \033[97m- No\n\n" +
                        "\033[95m")
        if inp_try.lower() == "y":
            return True
        elif inp_try.lower() == "n":
            return False
        else:
            print("\n\033[91mError. Invalid input.\033[97m\n")
            return self.retry()