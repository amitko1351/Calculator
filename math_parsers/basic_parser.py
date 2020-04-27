# Import Section
import re
from .math_validation import MathValidation

# Global Variable Section
UNARY_OPERATORS = ('+', '-')
DOT = '.'
MUL_SIGN = '*'
ONLY_SIGN_AFFECTED_NUMBER = '1'


# Code Section
class BasicParser:
    def __init__(self, operations: list, open_parenthesis: str='(', close_parenthesis: str=')'):
        self.operations = operations
        self.open_parenthesis = open_parenthesis
        self.close_parenthesis = close_parenthesis

    def parse_math_expr_to_list(self, math_expr: str) -> list:
        """
        The function prase the math experssion to a list
        :param math_expr: the math expression
        :return: None if the expression isn't legal otherwise return a list represent
        the expression
        """
        # Delete multi whitespaces
        math_expr = ' '.join(math_expr.split())
        # Check basic validation
        if not (self.__is_valid_expression(math_expr)):
            raise SyntaxError("Invalid math expression")
        parse_expr = self.__split_to_elements(math_expr)
        # Convert the numbers in the list to float
        self.__convert_list_elements_to_float(parse_expr)
        parse_expr = self.__parse_unary_operators(parse_expr)
        return parse_expr

    def __parse_unary_operators(self, parse_expr: list) -> list:
        """
        The function parse unary operation to <unary>1 * number
        :param parse_expr: the list to parse
        """
        index = 0
        while index < len(parse_expr):
            # Check if the operator can be unary
            if parse_expr[index] in UNARY_OPERATORS:
                # Check if there if the operator is unary
                if index == 0 or parse_expr[index - 1] == self.open_parenthesis:
                    sign = parse_expr[index]
                    parse_expr = parse_expr[:index] + [float(sign + ONLY_SIGN_AFFECTED_NUMBER), MUL_SIGN] + parse_expr[
                                                                                                            index + 1:]
                    index += 2
                    continue
            index += 1
        return parse_expr

    def __convert_list_elements_to_float(self, parse_expr: list):
        """
        Try to convert all the number in the list to float
        :param parse_expr: the list to convert
        """
        for i in range(len(parse_expr)):
            try:
                parse_expr[i] = float(parse_expr[i])
            except ValueError:
                pass

    def __split_to_elements(self, math_expr: str) -> list:
        """
        The function split the math_expr to all the elements ot the math experssion
        :param math_expr: the string of the math expression
        :return: list with the elements
        """
        regex_of_element = r'\d*\.\d+|\d+|[' + "".join(self.operations) + "]|[" + "".join([self.open_parenthesis,
                                                                                           self.close_parenthesis]) + "]"
        return re.findall(regex_of_element, math_expr)

    def __is_valid_expression(self, math_expr: str) -> bool:
        """
        The function check if the expression is valid base on the list of validation checks
        :param math_expr: the string of the math expression
        :return: True if valid otherwise false
        """
        return MathValidation.is_contains_only_numbers_and_operations(math_expr, self.operations,
                                                                      self.open_parenthesis, self.close_parenthesis) \
               and MathValidation.is_valid_parenthesis(math_expr, self.open_parenthesis, self.close_parenthesis)
