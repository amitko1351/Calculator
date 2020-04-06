# Import Section
from abc import ABC, abstractmethod
from MathModule import Math

# Global Variable Section
OPEN_PARENTHESIS = '('
CLOSE_PARENTHESIS = ')'


# Code Section
class Calculator(ABC):
    def __init__(self, operations_functions, operations_order):
        self._operations_functions = operations_functions
        self._operations_order = operations_order
        super().__init__()

    @abstractmethod
    def evaluate(self, math_expr):
        pass

    @abstractmethod
    def __doc__(self):
        pass


class BasicCalculator(Calculator):
    def __init__(self, operations_functions, operations_order):
        super().__init__(operations_functions, operations_order)

    def evaluate(self, math_expr):
        """
        The function evaluate the math expresion it gets
        :param math_expr: list of math expression -> [1, '+', 3]
        :return: the result of the math expression -> 4.0
        """
        global CLOSE_PARENTHESIS, OPEN_PARENTHESIS
        stack_expr = []  # Contain the expression used for the algorithm for scan parenthesis
        stack_open_parenthesis_pos = []  # Contain thr places of the open parenthesis
        for index in range(len(math_expr)):
            element = math_expr[index]
            if element == OPEN_PARENTHESIS:
                stack_expr.append(element)
                stack_open_parenthesis_pos.append(index)
            elif element == CLOSE_PARENTHESIS:
                last_open_parenthesis_pos = stack_open_parenthesis_pos.pop()
                result = self._eval_none_parenthesis_expr(stack_expr[last_open_parenthesis_pos + 1:])
                # Delete the Calculate part from the stack expression
                stack_expr = stack_expr[:last_open_parenthesis_pos]
                # Add the result to the stack expression
                stack_expr.append(result)
            else:
                stack_expr.append(element)
        if len(stack_expr) > 1:
            return self._eval_none_parenthesis_expr(stack_expr)
        return stack_expr.pop()

    def __eval_none_parenthesis_expr(self, math_expr):
        """
        The function calculates the math expression (assumption that there are no
        parenthesis in it)
        :param math_expr: math expression (assumption that there are no
        parenthesis in it) -> [1, '*', 4]
        :return: the result
        """
        for operations in self._operations_functions:
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
                    math_expr = math_expr[:index - 1] + [result] + math_expr[:index + 2]
                else:
                    index += 1
        return math_expr.pop()

    def __doc__(self):
        return """The Basic Calculator: Basic calculator that calculate expression which can include parenthesis"""
