from doctest import testmod
from data import Data
from data_validator import DataValidator
from staff_data import StaffData
from view_console import ViewConsole as view

# 1
def get_keys():
    """
    >>> get_keys()
    ['EMPID', 'AGE', 'GENDER', 'SALES', 'BMI', 'SALARY', 'BIRTHDAY']
    """
    return list(map(lambda i: i.name, Data))

# 2
def validate_bmi(bmi):
    """
    >>> validate_bmi("not a valid bmi")

    """
    v = DataValidator()
    return v.validators[Data.BMI.value](bmi)

# 3
def validate_salary(salary):
    """
    >>> validate_salary("three hundred")

    """
    v = DataValidator()
    return v.validators[Data.SALARY.value](salary)

# 4
def validate_all(raw_data):
    """
    >>> validate_all(["T123", 28, "M", 100, "heisobesity", "$350", "11-09-1990"])
    ['T123', 28, 'M', 100, 'Obesity', 350, '11-09-1990']
    """
    v = DataValidator()
    return v.check_all(raw_data)

# 5
def add_data(data):
    """
    >>> add_data(["T123", 28, "M", 100, "Obesity", "350", "11-09-1990"]) #doctest: +NORMALIZE_WHITESPACE
    [{'EMPID': 'T123', 'AGE': 28, 'GENDER': 'M', 'SALES': 100, 'BMI': 'Obesity',
    'SALARY': '350', 'BIRTHDAY': '11-09-1990'}]
    """
    sd = StaffData()
    sd.add_data(data)
    return sd.data

# 6
def get_gender():
    """
    >>> get_gender()
    {'Male': 2, 'Female': 1}
    """
    sd = StaffData()
    v = DataValidator()
    sd.add_data(v.check_all(["T133", 28, "M", 100, "Obesity", "350", "11-09-1990"]))
    sd.add_data(v.check_all(["T134", 29, "M", 150, "Normal", "300", "12-08-1989"]))
    sd.add_data(v.check_all(["T135", 30, "F", 100, "Normal", "300", "13-07-1988"]))
    return sd.get_gender()

# 7
def get_bmi():
    """
    >>> get_bmi()
    {'Obesity': 1, 'Normal': 2}
    """
    sd = StaffData()
    v = DataValidator()
    sd.add_data(v.check_all(["T133", 28, "M", 100, "Obesity", "350", "11-09-1990"]))
    sd.add_data(v.check_all(["T134", 29, "M", 150, "Normal", "300", "12-08-1989"]))
    sd.add_data(v.check_all(["T135", 30, "F", 100, "Normal", "300", "13-07-1988"]))
    return sd.get_bmi()

# 8
def display_error(txt):
    """
    >>> display_error("Error message")
    Error: Error message
    """
    return view.error(txt)

# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18


if __name__ == "__main__":
    testmod(verbose=True)
