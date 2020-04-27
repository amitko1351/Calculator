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

    def parse_function_expression(self, expression: str, functions: dict) -> str:
        """
        The function parse a function expression to a simple expression by parse the function to its translation
        :param functions: the function exist as a dict{name:MathFunction}
        :return: simple expression without function
        """
        # Delete whitespaces
        expression = ' '.join(expression.split())
        regex_to_find_functions = "(([a-z]+)\(((\d+|\d*\.\d+)([,]\d+|\d*\.\d+)*)\))"
        matches_functions = re.finditer(regex_to_find_functions, expression)
        for match_function in matches_functions:
            expression = self.__change_function_to_translation(expression, functions, match_function)
        return expression

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
        regex = f'^((([a-z]+)\(([a-z]+([,][a-z])*)\))=(([{"".join(self.__operations)}]|\d*\.\d+|\d+|' \
                f'[{self.__open_parenthesis}{self.__close_parenthesis}]|[' \
                f'a-z]+)+))$'
        name_group = 3
        params_group = 4
        expression_group = 6
        equation_structure = re.fullmatch(regex, equation)
        if equation_structure is None:
            raise TypeError("Invalid equation function")
        name = equation_structure.group(name_group)  # The group consist the name
        params = equation_structure.group(params_group).split(",")  # The group consist the params
        expression = equation_structure.group(expression_group)  # The group consist the expression
        return name, params, expression

    def __change_function_to_translation(self, expression: str, functions: dict, match_function) -> str:
        """
        The function change the match function in the expression to its translation  
        :param match_function: the match function found : match object of re
        :return: the expression with the function match translation 
        """
        full_match_group = 0
        name_group = 2
        params_group = 3
        function_name = match_function.group(name_group)
        function_params = match_function.group(params_group).split(',')
        # Change the params to float
        function_params = [float(param) for param in function_params]
        if function_name not in functions.keys():
            raise SyntaxError(f"Invalid expression, No function named {function_name}")
        # Translate function and add parenthesis to the translation
        function_translation = self.__open_parenthesis + functions[function_name].translate_expression(
            *function_params) + self.__close_parenthesis
        function_full_call = match_function.group(full_match_group)
        return expression.replace(function_full_call, function_translation)