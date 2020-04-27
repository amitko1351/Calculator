# Import Section
from math_function import MathFunction
import re
from .math_validation import FunctionValidation as fv
from calculators.calculator import Calculator


# Code Section
class FunctionParser:
    def __init__(self, operations: list, open_parenthesis: str = '(', close_parenthesis: str = ')'):
        self.__operations = operations
        self.__open_parenthesis = open_parenthesis
        self.__close_parenthesis = close_parenthesis

    def parse_equation_to_function(self, equation: str, calculator_to_check: Calculator) -> MathFunction:
        """
        Thr function parse an equation to math function -> a(b,c,d) = b + c + d
        :param calculator_to_check: calculator for checking the expression according to 
        :param equation: string describe the function -> a(b,c,d) = b + c + d
        :return: MathFunction object represent the function
        """
        # Delete whitespaces
        equation = ' '.join(equation.split())
        name, params, expression = self.__split_equation(equation)
        if not self.__is_valid_function(name, params, expression, calculator_to_check):
            raise SyntaxError("Invalid function")
        return MathFunction(name, params, expression)

    def __is_valid_function(self, name: str, params: list, expression: str, calculator_to_check: Calculator) -> bool:
        """
        The function check the validation of the function structure
        :param name: the name of the function
        :param params: the parameters of the function
        :param expression: the expression of the function
        :param calculator_to_check: calculator for checking the expression according to 
        :return: True if valid else False
        """
        return fv.is_valid_use_of_naming(name, self.__operations, self.__open_parenthesis, self.__close_parenthesis) and \
               fv.is_valid_parameters(params, self.__operations, self.__open_parenthesis, self.__close_parenthesis) and \
               fv.is_all_params_exist(params, expression, self.__operations, self.__open_parenthesis,
                                      self.__close_parenthesis) and \
               fv.is_valid_expression(expression, params, calculator_to_check)

    def __split_equation(self, equation: str) -> tuple:
        """
        The function split the equation to its components
        :param equation: string describe the function -> a(b,c,d) = b + c + d
        :return: the equation's components
        """
        regex = f'^((([a-z]+)\(([a-z]+([,]+[a-z])*)\))=(([{"".join(self.__operations)}]|\d*\.\d+|\d+|' \
                f'[{self.__open_parenthesis}{self.__close_parenthesis}]|[' \
                f'a-z]+)+))$'
        name_group = 3
        params_group = 4
        expression_group = 6
        equation_structure = re.fullmatch(regex, equation)
        if equation_structure is None:
            raise SyntaxError("Invalid equation function")
        name = equation_structure.group(name_group)  # The group consist the name
        params = equation_structure.group(params_group).split(",")  # The group consist the params
        expression = equation_structure.group(expression_group)  # The group consist the expression
        return name, params, expression
