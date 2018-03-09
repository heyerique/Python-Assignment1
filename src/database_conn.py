
import sqlite3


class Database:
    # Written By Vaishali
    #
    # This is the MySQL Database connection class
    #
    #
    def __init(self):
        # Written By Vaishali
        # The first method __init__() is a special method,
        # which is called class constructor or initialization method
        # creates to null veriable
        #
        self.conn = None
        self.cursor = None

    def create_db_connection(self, database_name):
        # Written by Vaishali
        #
        # This method to creates the connection with the database.
        #
        # Tries to handles the error if
        # no connection can be made. make the connection otherwise
        #
        # when database connect successfully then the conn atribute is given to
        # the connection object
        # and the cursor the cursor object.
        #
        # It then calls the make_tables method.
        #
        try:
            self.conn = sqlite3.connect(database_name)
            self.getconn = self.conn.cursor()
            self.make_tables()     # call make_table method here
            return False
        except ConnectionError:    # if connection fails
            print(ConnectionError) # print the error
        except TypeError as err:   # If type error
            print(err)             # Raised when an operation or function is attempted
                                   # that is invalid for the specified data type.

    def make_tables(self):
        # Written By Vaishali
        #
        # This is called from the create_db_connection method.
        # Create the employee table within the database.
        #
        # This only happens if the table doesnt exist.
        #
        #
        #    drop_table if exists

        make_table = """CREATE TABLE IF NOT EXISTS EMPLOYEE (empID VARCHAR(6),
                     Gender CHAR, age INTERGER, sales INTERGER, 
                     bmi VARCHAR(15), salary INTERGER, birthday DATE);"""
        self.getconn.execute (make_table)
        self.conn.commit ()



    def insert_employee_data(self):
        # Written By Vaishali
        #
        #
        #
        employee_data = [("A001","F","23","456","Normal","14","30/05/1994"),
                         ("A221","F","49","458","Normal","244","30/05/1994"),
                         ("C342","M","50","676","Overweight","300","1/12/1977"),
                         ("D123","F","55","123","Obesity","600","15/01/1997")]

        try:
            for person in employee_data:
                insert_string = """INSERT INTO employee (EMPID ,Gender, age, sales, bmi, salary, birthday)
                 VALUES ("{empID}", "{gender}", "{age}", "{sales}", "{bmi}",
                  "{salary}", "{birthday}");"""
                try:
                    insert_command = insert_string.format(empID=person[0],
                                                          gender=person[1],
                                                          age=person[2],
                                                          sales=person[3],
                                                          bmi=person[4],
                                                          salary=person[5],
                                                          birthday=person[6])
                    self.cursor.execute(insert_command)
                    self.conn.commit()
                except IndexError as err:
                    print(err)
                    return False

        except AttributeError as err:
            print(err)
            return False
        except UnboundLocalError as err:
            print(err)
            return False
        except TypeError as err:
            print(err)
            return False
        return True


    def select_employee_data(self):
        # Written By Vaishali
        #
        # This function retrieve all the employee data from the employee table
        # in array format and leter in the another function
        # the data will be set to the specific format

        data_arr = []    # Retrieve employee data in to data_arr "array" format
        try:
            self.cursor.execute("Select * from employee")
            result = self.cursor.fetchall()
            for r in result:
                data_arr.append(r)
            return data_arr
        except AttributeError as err:
            print(err)
            return False




# connection.close()