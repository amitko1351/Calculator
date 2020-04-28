# Import Section
from .basic_calculator import BasicCalculator
import pickle
import os
from math_parsers import FunctionParser
import itertools
from math_function import MathFunction


# Global Section


# Code Section
class FunctionCalculator(BasicCalculator):
    FILE_OF_SAVED_FUNCTION = "./functions.dat"

    def __init__(self, operations_functions: dict, operations_order: list):
        super().__init__(operations_functions, operations_order)
        self.__functions = self.__lode_from_file()
        self.__function_parser = FunctionParser(list(itertools.chain.from_iterable(self._operations_order)),
                                                self.OPEN_PARENTHESIS,
                                                self.CLOSE_PARENTHESIS)

    def evaluate(self, math_expr: str) -> str or float:
        """
        The function evaluate the expression
        :param math_expr: the math expression or function expression
        :return: string if add the function or float result of the expression
        """
        # Try to see if the expression is a function initialization
        try:
            new_function = self.__function_parser.parse_equation_to_function(math_expr, self)
            self.__add_function(new_function)
            return "Saved"
        except TypeError:
            # If cannot make new function it is a function expression
            math_expr = self.__function_parser.parse_function_expression(math_expr, self.__functions)
            return super().evaluate(math_expr)

    def __lode_from_file(self) -> dict:
        """
        The function lode the data in the file if exist other wise return an empty dict
        """
        # Check if the file exist
        if not (os.path.exists(FunctionCalculator.FILE_OF_SAVED_FUNCTION) and os.path.isfile(
                FunctionCalculator.FILE_OF_SAVED_FUNCTION)):
            return dict()
        with open(FunctionCalculator.FILE_OF_SAVED_FUNCTION, "rb") as f:
            functions = pickle.load(f)
        if functions is None:
            return dict()
        return functions

    def __add_function(self, new_function: MathFunction):
        """
        The function add a new function to the function list and save the list
        :param new_function: the new function to save
        """
        self.__functions[new_function.get_name()] = new_function
        with open(FunctionCalculator.FILE_OF_SAVED_FUNCTION, "wb") as f:
            pickle.dump(self.__functions, f)

    @staticmethod
    def __doc__():
        return """Function Calculator : base on the Basic Calculator and can use function and create ones (by name(
        params)=expression)"""
