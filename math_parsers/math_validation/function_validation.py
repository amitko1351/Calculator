# Import Section
import re
from .validation import MathValidation
from calculators.calculator import Calculator


# Code Section
class FunctionValidation:
    @staticmethod
    def is_all_params_exist(params: list, expression: str, operation: list, open_parenthesis: str,
                            close_parenthesis: str) -> bool:
        """
        The function check if params in the expression exist in the params list
        :param operation: operation possible
        :param params: the params list
        :param expression: the expression to check
        :return: True if all the params in the expression in the the params list
        """
        # Put a number instant of all the params in the list
        number = 1
        for param in params:
            expression = re.sub(f'{param}', f'{number}', expression)
        # Check if there are params left in expression that are not in the params list
        return MathValidation.is_contains_only_numbers_and_operations(expression, operation, open_parenthesis,
                                                                      close_parenthesis)

    @staticmethod
    def is_valid_parameters(params: list, operations: list, open_parenthesis: str, close_parenthesis: str) -> bool:
        """
        Thr function check if the parameters are valid not an operation or a parenthesis
        :param params: the list of the parameters
        :param operation: the valid operation
        :return: True if the parameters are valid
        """
        for param in params:
            if not FunctionValidation.is_valid_use_of_naming(param, operations, open_parenthesis, close_parenthesis):
                return False
        return True

    @staticmethod
    def is_valid_use_of_naming(name: str, operations: list, open_parenthesis: str, close_parenthesis: str) -> bool:
        """
        Thr function check if the name used isn't used in the other operation of the calculator
        :param name: the name to check
        :param operations: the valid operation
        :param open_parenthesis: open parenthesis 
        :param close_parenthesis: close parenthesis 
        :return: True if the naming is valid 
        """
        return name not in operations and name != open_parenthesis and name != close_parenthesis

    @staticmethod
    def is_valid_expression(expression: str, params: list, calculator_to_check: Calculator) -> bool:
        """
        The function check if the expression is valid
        :param expression: thr expression to check
        :param params: the params list
        :param calculator_to_check: calculator for checking the expression according to  
        :return: True if valid otherwise False
        """
        # Put a number instant of all the params in the list
        number = 0
        for param in params:
            expression = re.sub(f'{param}', f'{number}', expression)
        try:
            calculator_to_check.evaluate(expression)
        except SyntaxError:
            return False
        return True
