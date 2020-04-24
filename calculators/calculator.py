# Import Section
from abc import ABC, abstractmethod


# Code Section
class Calculator(ABC):
    def __init__(self, operations_functions: dict, operations_order: list):
        self._operations_functions = operations_functions
        self._operations_order = operations_order
        super().__init__()

    @abstractmethod
    def evaluate(self, math_expr: str) -> str or float or int:
        pass

    @staticmethod
    @abstractmethod
    def __doc__() -> str:
        pass
