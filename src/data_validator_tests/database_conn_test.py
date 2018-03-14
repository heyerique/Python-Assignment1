#!usr/bin/python
from Database_conn.database import Database
# from Model.DatabaseConn.database import database
# By Vaishali
import sqlite3


class database():

    def __init__(self):
        self_conn = None
        self_cursor = None  # prepare a cursor object using cursor() method

    def create_dbConnection(self, database_name):
        try:
            self.conn = sqlite3.connect(database_name)
        except ConnectionError:
            print (ConnectionError)
            # prepare a cursor object using cursor() method
            self.cursor = self.conn.cursor()
            self.make_tables()

    # Drop table if it already exist using execute() method.
    # self.cursor.execute("Drop table employee if exists!")

    # Create table name "employee" as per requirement
    def make_tables(self):
        make_table = """CREATE TABLE IF NOT EXISTS employee (
            EMPID INTERGER PRIMARY KEY, Gender CHAR, sales INTERGER
            , bmi VARCHAR(15), salary INTERGER, birthday DATE);"""
        try:
            # Execute the SQL Command
            self.cursor.execute(make_table)
            self.conn.commit()  # Commit the changes in database
            # Commit is the operation, which gives a green signal
            # to database to finalize the changes, and after this operation,
            # no change can be reverted back.
        except:
            # Rollback in case there is any error
            # If you are not satisfied with one or more of the changes
            # and you want to revert back those changes completely,
            # then use rollback() method.
            self.conn.rollback()

    # insert into employee table by defining emplayee_arrey
    def insert_employee(self):
        for employee in data_arr:
            insert_string =
            """INSERT INTO employees (empid, Gender, sales, bmi, salary, birthday)VALUES
                (NULL, "{gender}", "{sales}", "{bmi}", "{salary}", "{birthday}
                "); """
            insert_command = insert_string.format(gender=employee[1],
                                                  sales=employee[3],
                                                  bmi=employee[4],
                                                  salary=employee[5],
                                                  birthday=employee[6])
        try:
            # Execute the SQL Command
            self.cursor.execute(insert_string)
            self.conn.commit()  # Commit the changes in database
        except:
            # Rollback in case there is any error
            self.conn.rollback()

    # retrive dara from employee_arr[]
    def select_employee_data(self):
        data_arr = []
        try:
            # Execute the SQL Command
            self.cursor.execute("""SELECT * FROM employee""")
            # Fetch all the rows in a list of lists.
            result = cursor.fetchall()
            for r in result:
                data_arr.append(r)      # append data into employee_arrey[]
                return data_arr

        except:
            # Rollback in case there is any error
            self.conn.rollback()

    def get_employee_information(self, database_name='mydb'):
        self.create_connection(database_name)
        return self.select_person_data()

    def save_data(self, data_arr, database_name='mydb'):
        self.create_connection(database_name)
        try:
            self.insert_person(data_arr)
            return "Success"
        except RuntimeError:
            print("Error inserting the data into the database")
            return "Error"
