# Import Section
import re


# Code Section
class MathFunction:
    def __init__(self, name: str, params: list, expression: str):
        """
        :param name: The name of the function
        :param params: the params of the function in order -> [a,b,c]
        :param expression: the expression of the function -> a+b+c
        """
        self.__name = name
        self.__expression = self.__translate_expression(params, expression)
        self.__number_of_params = len(params)
        # Translate the expression for the function class

    def __translate_expression(self, params: list, expression: str) -> str:
        """
        The function translate the expression of a+b+c to be formated {1}+{2}+{3}
        :param params: the params of the function
        :param expression: the expression of the function 
        :return format expression
        """
        for index in range(len(params)):
            expression = re.sub(f'({params[index]})', f'{{{index}}}', expression)
        return expression

    def translate_expression(self, *params) -> str:
        """
        The function translate the math function to math expression with thw params
        :param params: the params of the math function
        :return: string of the expression in which the values has been set
        """
        if len(params) != self.__number_of_params:
            TypeError(f"Invalid number of parameters pass to the function named {self.__name}")
        return self.__expression.format(*params)

    def get_name(self) -> str:
        """
        The function return the function name
        :return: thr function name
        """
        return self.__name
