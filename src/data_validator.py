import re
from data import Data

class DataValidator:
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

    def check_all(self, all_data):
        """
        Check validation of the all data. Throw ValueError Exceptions.
        :param all_data: a data list
        :return: washed data in dictionary
        :Author: Zhiming Liu
        """
        # Save the washed data temporarily
        data = []

        # String template for exceptions
        error_str = "Error: %s is not a valid value."

        # Check and wash EMPID
        value = self.check_empid(all_data[0])
        # Raise an exception if the return value is None,
        # Otherwise save to the temporary data
        if value == None:
            raise ValueError(error_str % "EMPID")
        else:
            data.append(value)

        # Check and wash age
        value = self.check_age(all_data[1])
        # Raise an exception if the return value is None,
        # Otherwise save to the temporary data
        if value == None:
            raise ValueError(error_str % "Age")
        else:
            data.append(value)

        # Check and wash gender
        value = self.check_gender(all_data[2])
        # Raise an exception if the return value is None,
        # Otherwise save to the temporary data
        if value == None:
            raise ValueError(error_str % "Gender")
        else:
            data.append(value)

        # Check and wash sales
        value = self.check_sales(all_data[3])
        # Raise an exception if the return value is None,
        # Otherwise save to the temporary data
        if value == None:
            raise ValueError(error_str % "Sales")
        else:
            data.append(value)

        # Check and wash BMI
        value = self.check_bmi(all_data[4])
        # Raise an exception if the return value is None,
        # Otherwise save to the temporary data
        if value == None:
            raise ValueError(error_str % "BMI")
        else:
            data.append(value)

        # Check and wash salary
        value = self.check_salary(all_data[5])
        # Raise an exception if the return value is None,
        # Otherwise save to the temporary data
        if value == None:
            raise ValueError(error_str % "Salary")
        else:
            data.append(value)

        # Check and wash birthday
        value = self.check_birthday(all_data[6])
        # Raise an exception if the return value is None,
        # Otherwise save to the temporary data
        if value == None:
            raise ValueError(error_str % "Birthday")
        else:
            data.append(value)

        return data


# print(DataValidator.check_bmi("jbjndsoidiri88888normaljdjdjd"))
# v = DataValidator()
# print(v.check_all("$001TT TW"))
