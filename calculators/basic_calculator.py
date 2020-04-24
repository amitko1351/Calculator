# Import Section
import itertools
from math_operators import Math
from math_parsers import BasicParser
from .calculator import Calculator

# Global Variable Section
OPEN_PARENTHESIS = '('
CLOSE_PARENTHESIS = ')'


class BasicCalculator(Calculator):
    def __init__(self, operations_functions: dict, operations_order: list):
        super().__init__(operations_functions, operations_order)
        self.parser = BasicParser(list(itertools.chain.from_iterable(self._operations_order)), OPEN_PARENTHESIS,
                                  CLOSE_PARENTHESIS)

    def evaluate(self, math_expr: str) -> float:
        """
        The function evaluate the math_operators expresion it gets
        :param math_expr: string of math_operators expression -> '1+3'
        :return: the result of the math_operators expression -> 4.0
        """
        # Parse the expression
        math_expr = self.parser.parse_math_expr_to_list(math_expr)
        try:
            return self.__eval_parenthesis_expr(math_expr)
        except (IndexError, TypeError):
            raise SyntaxError("Invalid math_operators expression")

    def __eval_parenthesis_expr(self, math_expr: list) -> float:
        """
        The function calculates the math_operators expression 
        :param math_expr: math_operators expression represent as a list -> ['-', '(', 9, '-', '(', 3, '+', 7, ')']
        :return: the result
        """
        global CLOSE_PARENTHESIS, OPEN_PARENTHESIS
        stack_expr = []  # Contain the expression used for the algorithm for scan parenthesis
        stack_open_parenthesis_pos = []  # Contain thr places of the open parenthesis
        for element in math_expr:
            if element == OPEN_PARENTHESIS:
                stack_expr.append(element)
                stack_open_parenthesis_pos.append(len(stack_expr) - 1)
            elif element == CLOSE_PARENTHESIS:
                last_open_parenthesis_pos = stack_open_parenthesis_pos.pop()
                result = self.__eval_none_parenthesis_expr(stack_expr[last_open_parenthesis_pos + 1:])
                # Delete the Calculate part from the stack expression
                stack_expr = stack_expr[:last_open_parenthesis_pos]
                # Add the result to the stack expression
                stack_expr.append(result)
            else:
                stack_expr.append(element)
        if len(stack_expr) > 1:
            return self.__eval_none_parenthesis_expr(stack_expr)
        return stack_expr.pop()

    def __eval_none_parenthesis_expr(self, math_expr: list) -> float:
        """
        The function calculates the math_operators expression (assumption that there are no
        parenthesis in it)
        :param math_expr: math_operators expression (assumption that there are no
        parenthesis in it) -> [1, '*', 4]
        :return: the result
        """
        for operations in self._operations_order:
            index = 1
            while index < (len(math_expr)):
                element = math_expr[index]
                if element in operations:
                    # Get the function by his name
                    operation_function = getattr(Math, self._operations_functions[element])
                    # Activate the function on thr number beside the operation
                    result = operation_function(math_expr[index - 1], math_expr[index + 1])
                    # Slice the list so the expression calculated be delete and instead the result be in the list
                    # example : [1, '+', 4, '/', 2] --> [1, '+', 2]
                    math_expr = math_expr[:index - 1] + [result] + math_expr[index + 2:]
                else:
                    index += 1
        if len(math_expr) == 1:
            return math_expr.pop()
        raise SyntaxError("Invalid math expression")

    @staticmethod
    def __doc__() -> str:
        return """The Basic Calculator: Basic calculator that calculate expression which can include parenthesis"""
