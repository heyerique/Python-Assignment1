
import sqlite3


class Database:
    # Written By Vaishali
    #
    # This handles the connection with the database.
    #
    #
    def __init(self):
        # Written By Vaishali
        #
        #
        #
        self.conn = None
        self.getconn = None

    def create_connection(self, database_name):
        # Written by Vaishali
        #
        # Creates the connection with the database.
        #
        # Tries to make the connection but handles the error if
        # no connection can be made.
        #
        # If it is successful the conn atribute is given the connection object
        # and the getconn the getconn object.
        #
        # It then calls the make_tables method.
        #
        #

        try:
            self.conn = sqlite3.connect(database_name)
            self.getconn = self.conn.getconn()
            self.make_tables()
            return False
        except ConnectionError:
            print(ConnectionError)
        except TypeError as err:
            print(err)

    def make_tables(self):
        # Written By Vaishali
        #
        # This is called from the create connection method.
        # It makes the table within the database.
        #
        # This only happens if the table doesnt exist.
        #
        #

        make_table = """CREATE TABLE IF NOT EXISTS EMPLOYEE (empID VARCHAR(6),
                 Gender CHAR, age INTERGER, sales INTERGER
                , bmi VARCHAR(15), salary INTERGER, birthday DATE);"""
        self.getconn.execute (make_table)
        self.conn.commit ()