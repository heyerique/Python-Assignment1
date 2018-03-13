# By Vaishali
# DocTest
from Model.DataValidation.data_validator import IDataValidator
import re
import doctest
doctest.testfile("Model/DataValidation/employee.txt")


class Test:
    """
    >>> a=Test(5)
    >>> a.multiply_by_2()
    10
    """
    def __init__(self, number):
        self._number = number

    def multiply_by_2(self):
        return self._number*2


class DataValidator(IDataValidator):

    # Check valid empid
    def validate_empid(empid):
        """
        EMPID = [A-Z][0-9]{3}) e.g. A001
        >>> DataValidator.validate_empid("A001")
        True
        """
        if re.compile("^[A-Z][0-9]{3}$").match(empid):
            return True
        else:
            return False

    # Check valid gender M / F
    def validate_gender(gender):
        """
        gender = M or F e.g. M or F
        >>> DataValidator.validate_gender("F")
        True
        """
        if re.compile("^[M|F]").match(gender):
            return True
        else:
            return False

    # Check valid age
    def validate_age(age):
        """
        age = [0-9]{2} e.g. 0 to 99
        >>> DataValidator.validate_age(str(64))
        True
        """
        if re.compile("^[0-9]{2}$").match(age):
            return True
        else:
            return False

    # Check valid sales
    def validate_sales(sales):
        """
        Sales = [0-9]{3} e.g. 330
        >>> DataValidator.validate_sales(str(999))
        True
        """
        if re.compile("^[0-9]{3}$").match(sales):
            return True
        else:
            return False

    # Check valid BMI
    def validate_bmi(bmi):
        """
        BMI = normal|overweight|obesity|underweight

        >>> DataValidator.validate_bmi("Overweight")
        True
        """
        if re.compile("^Normal|Overweight|Obesity|Underweight$").match(bmi):
            return True
        else:
            return False

    # Check valid salary
    def validate_salary(salary):
        """
        Salary = [0-9]{2,3} e.g. 33 or 330
        >>> DataValidator.validate_salary(str(24))
        True
        """
        if re.compile("^[0-9]{2,3}$").match(salary):
            return True
        else:
            return False

    # Check valid Birthday
    def validate_birthday(birthday):
        """
        birthday = [0-9]{1,2}-[0-9]{1,2}-[0-9]{4} e.g. 2-5-1967
        >>> DataValidator.validate_birthday("2-6-2014")
        True
        """
        if re.compile("^([0-9]{1,2})-([0-9]{1,2})-"
                      "([0-9]{4})$").match(birthday):
            return True

        else:
            return False

if __name__ == "__main__":
        doctest.testmod()