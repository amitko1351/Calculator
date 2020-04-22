# Global Section
DOT = '.'

# Code Section
class MathValidation:
    @staticmethod
    def is_valid_parenthesis(math_expr, open_parenthesis, close_parenthesis):
        """
        The function check if the parenthesis in the math expression is valid
        :param close_parenthesis: the char of the close parenthesis
        :param open_parenthesis: the char of the open parenthesis
        :param math_expr: the math expression as string
        :return: True if valid else False
        """
        stack_open_parenthesis = []
        for element in list(math_expr):
            if element == open_parenthesis:
                stack_open_parenthesis.append(element)
            elif element == close_parenthesis:
                try:
                    stack_open_parenthesis.pop()
                except IndexError:
                    return False
        return len(stack_open_parenthesis) == 0

    @staticmethod
    def is_contains_only_numbers_and_operations(math_expr, operations, open_parenthesis, close_parenthesis):
        """
        The function check if all the char are only numbers and operations
        :param close_parenthesis: the char of the close parenthesis
        :param open_parenthesis: the char of the open parenthesis
        :param math_expr: the math expression
        :param operations: the valid operations
        :return: True if valid else False
        """
        global DOT
        for element in list(math_expr):
            if not (element in operations or element == close_parenthesis or
                            element == open_parenthesis or element.isdigit() or element == DOT):
                return False
        return True
