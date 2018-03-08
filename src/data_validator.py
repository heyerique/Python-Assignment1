import re

class DataValidator:
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
        bmi = str(input_bmi)
        pattern = r".*(?P<bmi>normal|overweight|obesity|underweight).*"
        match_obj = re.search(pattern, bmi, re.I)
        if match_obj:
            bmi = match_obj.group("bmi") # Find the match
            bmi = " ".join(text[0].upper() + text[1:] for text in bmi.split()) # Capitalise the first letter
            return bmi
        return None

    @staticmethod
    def check_salary(input_salary):
        """
        Check if the input salary is valid.
        :param input_salary: user input
        :return: Formatted salary if the input one is valid, otherwise, return None
        :Author: Zhiming Liu
        """
        salary = input_salary
        pattern = r"\D(?P<salary>[0-9]{2,3})\D"
        match_obj = re.search(pattern, salary)
        if match_obj:
            return match_obj["salary"]
        return None

    @staticmethod
    def check_birthday(birthday):
        return birthday


# print(DataValidator.check_bmi("jbjndsoidiri88888normaljdjdjd"))
# print(DataValidator.check_salary("$001TT TW"))
