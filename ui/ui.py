# Import Section
import json
import sys

# Global Section
MARGIN = 7


# Code Section

class UI:
    def __init__(self, calculators: list, calculator_methods_conf_file: str):
        self.__calculators = calculators
        self.__operate_calculator = None
        # Read form the configuration file given
        with open(calculator_methods_conf_file) as json_conf_file:
            self.__calculator_methods = json.load(json_conf_file)

    def __show_open_message(self):
        """
        Print the open message
        """
        welcome_message = "Welcome to the Cool Calculator"
        self.print_header(welcome_message)

    def print_header(self, header: str):
        """
        The function print thr header in the format
        --------------------------------------------
               Welcome to the Cool Calculator
        --------------------------------------------
        :param header: the header to print
        """
        global MARGIN
        border_size = MARGIN * 2 + len(header)
        print("-" * border_size)
        print((" " * MARGIN) + header)
        print("-" * border_size)

    def main_loop(self):
        """
        The function active the loop of the UI
        """
        self.__show_open_message()
        while True:
            chose_calculator = self.__choose_calculator()
            chose_calculator_method = self.__choose_calculator_method()
            # Loop until exit thr calculator
            self.__active_calculator(chose_calculator, chose_calculator_method)

    def __choose_calculator(self) -> type:
        """
        The function let the user choose the calculator type 
        :return: the type of calculator choose
        """
        while True:
            self.print_header("Please enter the calculator you want to use")
            # Display options
            for index in range(len(self.__calculators)):
                print("Enter - {} for {}.".format(str(index), self.__calculators[index].__doc__()))
            # Get the choice
            index_chose_calculator = input("Your choice ->")
            # Check validation
            if index_chose_calculator.isdigit() and 0 <= int(index_chose_calculator) < len(self.__calculators):
                return self.__calculators[int(index_chose_calculator)]
            # Invalid input
            print("Invalid input, please make to sure to enter the correct number", file=sys.stderr)

    def __choose_calculator_method(self) -> str:
        """
        The function let the user choose the method of calculation
        :return: the method of calculation chose
        """
        while True:
            self.print_header("Please enter the method of calculation you want to use")
            # Display options
            calculation_methods_names = list(self.__calculator_methods.keys())
            for index in range(len(calculation_methods_names)):
                print("Enter - {} for {}.".format(str(index), self.__calculator_methods[calculation_methods_names[
                    index]]["doc"]))
            # Get the choice
            index_chose_method = input("Your choice ->")
            # Check validation
            if index_chose_method.isdigit() and 0 <= int(index_chose_method) < len(calculation_methods_names):
                return calculation_methods_names[int(index_chose_method)]
            # Invalid input
            print("Invalid input, please make to sure to enter the correct number", file=sys.stderr)

    def __active_calculator(self, chose_calculator: type, chose_calculator_method: str):
        """
        The function activate the calculator chose 
        :param chose_calculator: the class of the chose calculator
        :param chose_calculator_method: the name of the chose calculator method 
        """
        # Create the Calculator chose
        self.__operate_calculator = chose_calculator(
            self.__calculator_methods[chose_calculator_method]["operations_functions"],
            self.__calculator_methods[chose_calculator_method]["operations_order"])
        self.print_header("Calculator activated")
        while True:
            print("Please enter the math expression to calculate or exit to change calculator")
            experssion = input("->")
            if experssion == "exit":
                break
            try:
                print("result -> {}".format(str(self.__operate_calculator.evaluate(experssion))))
            except SyntaxError as e:
                print(e.msg)
            except ZeroDivisionError as e:
                print("Can't divided by zero")
