from abc import ABC, abstractmethod


class Calculator(ABC):
    def __init__(self, operations_functions, operations_order):
        self._operations_functions = operations_functions
        self._operations_order = operations_order
        super().__init__()

    @abstractmethod
    def evaluate(self, math_expr):
        pass
