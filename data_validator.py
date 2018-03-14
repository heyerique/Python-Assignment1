import re
from data import Data

class DataValidator:

    def __init__(self):
        # A function list if validators
        self.validators = (
            self.check_empid, self.check_gender, self.check_age,
            self.check_sales, self.check_bmi, self.check_salary,
            self.check_birthday
        )

    @staticmethod
    def check_empid(empid):
        return empid

    @staticmethod
    def check_gender(gender):
        return gender

    @staticmethod
    def check_age(age):
        return age

    @staticmethod
    def check_sales(sales):
        return sales

    @staticmethod
    def check_bmi(input_bmi):
        """
        Check if the input BMI is valid.
        :param input_bmi: user input
        :return: Formatted BMI if the input one is valid, otherwise, return None
        :Author: Zhiming Liu
        """
        # Convert the input data to string
        bmi = str(input_bmi)

        # Regular expression checks if any of the specified keywords exists
        # :P<bmi> Assign to the group with the keyword 'bmi'
        pattern = r".*(?P<bmi>normal|overweight|obesity|underweight).*"
        match_obj = re.search(pattern, bmi, re.I)
        if match_obj:
            # Get the matched word
            bmi = match_obj.group("bmi")
            # Convert the first letter to uppercase and lowercase for rest of them
            bmi = " ".join(text[0].upper() + text[1:] for text in bmi.split()) # Capitalise the first letter
            return bmi
        # Return None if no match found
        return None

    @staticmethod
    def check_salary(input_salary):
        """
        Check if the input salary is valid.
        :param input_salary: user input
        :return: Formatted salary if the input one is valid, otherwise, return None
        :Author: Zhiming Liu
        """
        # Regular expression checks if there are consecutive 3 numbers
        # :P<salary> Assign to the group with the keyword 'salary'
        pattern = r"\D*(?P<salary>[0-9]{2,3})\D*"
        match_obj = re.search(pattern, input_salary)
        if match_obj:
            # Convert the match to integer and return
            return int(match_obj.group("salary"))
        # Return None if no match found
        return None

    @staticmethod
    def check_birthday(birthday):
        return birthday

    def check_all(self, all_data: list):
        """
        Check validation of the all data. Throw ValueError Exceptions.
        :param all_data: a data list
        :return: washed data in dictionary
        :Author: Zhiming Liu
        """
        # Save the washed data temporarily
        result = []

        # If the number of the data is not correct, return an empty result
        if not len(all_data) == len(Data):
            return result

        # Check and wash data
        key = 0
        while key < len(all_data):
            # Get the validation function by the order of the data
            v = self.validators[key]
            # Append to the result
            result.append(v(all_data[key]))
            key += 1

        return result


# print(DataValidator.check_bmi("jbjndsoidiri88888normaljdjdjd"))
# v = DataValidator()
# print(v.check_all("$001TT TW"))
