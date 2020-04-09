# Import Section
import re

# Global Variable Section
OPEN_PARENTHESIS = '('
CLOSE_PARENTHESIS = ')'
UNARY_OPERATORS = ('+', '-')
DOT = '.'
MUL_SIGN = '*'
ONLY_SIGN_AFFECTED_NUMBER = '1'

# Code Section
class BasicParser:
    @staticmethod
    def parse_math_expr_to_list(math_expr, operations):
        """
        The function prase the math experssion to a list
        :param math_expr: the math expression
        :param operations: legal operations
        :return: None if the expression isn't legal otherwise return a list represent
        the expression
        """
        # Delete multi whitespaces
        math_expr = ' '.join(math_expr.split())
        # Check basic validation
        if not (BasicParser.__is_valid_parenthesis(math_expr) and BasicParser.__is_valid_char(math_expr, operations)):
            raise SyntaxError("Invalid math expression")
        parse_expr = BasicParser.__split_to_elements(math_expr, operations)
        # Convert the numbers in the list to float
        BasicParser.__convert_list_elements_to_float(parse_expr)
        parse_expr = BasicParser.__parse_unary_operators(parse_expr)
        return parse_expr

    @staticmethod
    def __parse_unary_operators(parse_expr):
        """
        The function parse unary operation to <unary>1 * number
        :param parse_expr: the list to parse
        """
        index = 0
        while index < len(parse_expr):
            # Check if the operator can be unary
            if parse_expr[index] in UNARY_OPERATORS:
                # Check if there if the operator is unary
                if index == 0 or parse_expr[index - 1] == OPEN_PARENTHESIS:
                    sign = parse_expr[index]
                    parse_expr = parse_expr[:index] + [float(sign + ONLY_SIGN_AFFECTED_NUMBER), MUL_SIGN] + parse_expr[index+1:]
                    index += 2
                    continue
            index += 1
        return parse_expr

    @staticmethod
    def __convert_list_elements_to_float(parse_expr):
        """
        Try to convert all the number in the list to float
        :param parse_expr: the list to convert
        """
        for i in range(len(parse_expr)):
            try:
                parse_expr[i] = float(parse_expr[i])
            except ValueError:
                pass

    @staticmethod
    def __split_to_elements(math_expr, operations):
        """
        The function split the math_expr to all the elements ot the math experssion
        :param math_expr: the string of the math expression
        :param operations: the operations
        :return: list with the elements
        """
        regex_of_element = r'\d+|[' + "".join(operations) + "]|\d*\.\d+|[" + "".join([OPEN_PARENTHESIS,
                                                                                      CLOSE_PARENTHESIS]) + "]"
        return re.findall(regex_of_element, math_expr)

    @staticmethod
    def __is_valid_char(math_expr, operations):
        """
        The function check if all the char are valid 
        :param math_expr: the math expression
        :param operations: the valid operations
        :return: True if valid else False
        """
        for element in list(math_expr):
            if not (element in operations or element == CLOSE_PARENTHESIS or
                            element == OPEN_PARENTHESIS or element.isdigit() or element == DOT):
                return False
        return True

    @staticmethod
    def __is_valid_parenthesis(math_expr):
        """
        The function check if the parenthesis in the math expression is valid
        :param math_expr: the math expression
        :return: True if valid else False
        """
        stack_open_parenthesis = []
        for element in list(math_expr):
            if element == OPEN_PARENTHESIS:
                stack_open_parenthesis.append(element)
            elif element == CLOSE_PARENTHESIS:
                try:
                    stack_open_parenthesis.pop()
                except IndexError:
                    return False
        return len(stack_open_parenthesis) == 0
