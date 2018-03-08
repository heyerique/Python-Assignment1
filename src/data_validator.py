import re

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
        pattern = r"\D*(?P<salary>[0-9]{2,3})\D*"
        match_obj = re.search(pattern, salary)
        if match_obj:
            return int(match_obj.group("salary"))
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
        data = {}
        error_str = "Error: %s is not a valid value."

        value = self.check_empid(all_data[0])
        if value == None:
            raise ValueError(error_str % "EMPID")
        else:
            data["empid"] = value

        value = self.check_age(all_data[1])
        if value == None:
            raise ValueError(error_str % "Age")
        else:
            data["age"] = value

        value = self.check_gender(all_data[2])
        if value == None:
            raise ValueError(error_str % "Gender")
        else:
            data["gender"] = value

        value = self.check_sales(all_data[3])
        if value == None:
            raise ValueError(error_str % "Sales")
        else:
            data["sales"] = value

        value = self.check_bmi(all_data[4])
        if value == None:
            raise ValueError(error_str % "BMI")
        else:
            data["bmi"] = value

        value = self.check_salary(all_data[5])
        if value == None:
            raise ValueError(error_str % "Salary")
        else:
            data["salary"] = value

        value = self.check_birthday(all_data[6])
        if value == None:
            raise ValueError(error_str % "Birthday")
        else:
            data["birthday"] = value

        return data


# print(DataValidator.check_bmi("jbjndsoidiri88888normaljdjdjd"))
# v = DataValidator()
# print(v.check_all("$001TT TW"))
