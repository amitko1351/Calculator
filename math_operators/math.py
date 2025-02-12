class Math:
    """
    Contain math operations 
    """
    @staticmethod
    def add(num1: float or int, num2: float or int) -> float or int:
        """
        The function do addition operation on the two number 
        num1 + num2
        :return: the addition result
        """
        return num1 + num2

    @staticmethod
    def sub(num1: float or int, num2: float or int) -> float or int:
        """
        The function do subtraction operation on the two number 
        num1 - num2
        :return: the subtraction result
        """
        return num1 - num2

    @staticmethod
    def div(num1: float or int, num2: float or int) -> float or int:
        """
        The function do division operation on the two number 
        num1 / num2
        :return: the division result as float type
        """
        return float(num1) / num2

    @staticmethod
    def mul(num1: float or int, num2: float or int) -> float or int:
        """
        The function do multiplication operation on the two number 
        num1 / num2
        :return: the multiplication result
        """
        return num1 * num2
