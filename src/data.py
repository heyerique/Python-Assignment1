from enum import Enum, unique

@unique
class Data(Enum):
    """
    Enum for data
    :Author: Zhiming Liu
    """
    EMPID = 0
    AGE = 1
    GENDER = 2
    SALES = 3
    BMI = 4
    SALARY = 5
    BIRTHDAY = 6
