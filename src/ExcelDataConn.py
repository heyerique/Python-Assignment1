from Model.Database import IDatabase
import xlsxwriter


class Database(IDatabase):
    # Written By Vaishali
    def __init__(self):
        # Initialize the row and col Varible so
        # that I can reassign them when require
        self.row = 0
        self.col = 0

    # Written By Vaishali
    #
    # Create a new workbook object using the workbook() constructor
    # Workbook()takes one, non-optional argument
    # which is the filename that we want to create
    #
    # xlswriter can only make new file. It can't read or modify existing file
    #
    # By Default, worksheet name is bydefault i.e. workshhet1,
    # worksheet2 etc. But we can also specify a name
    # worksheet1 = workbook.add.worksheet(personData)
    #
    # Somedata we want to write to the worksheet1

    def createWorkbook(self):
        # Written By Vaishali
        workbook = xlsxwriter.Workbook('Employee.xlsx')

    def createWorksheet(self):
        # Written By Vaishali
        worksheet1 = workbook.add.worksheet(EmployeeData)

# Write some data headers.
worksheet.write('A1', 'EmployeeID', bold)
worksheet.write('B1', 'Gender', bold)
worksheet.write('C1', 'Age', bold)
worksheet.write('D1', 'Sales', bold)
worksheet.write('E1', 'BMI', bold)
worksheet.write('F1', 'Salary', bold)
worksheet.write('G1', 'Birthday', bold)

# Some data we want to write to the worksheet.
Employee = (
    ['EMPID', 'E1001'],
    ['Gender', 'F'],
    ['Age', 25],
    ['Sales', 50],
    ['BMI', 'Normal'],
    ['Salary', 850],
    ['Birthday', '1999-03-03'],
)

# Iterate over the data and write it out row by row.
for EMPID, Gender, Age, Sales, BMI, Salary, Birthday in (Employee):
    # Convert the date string into a datetime object.
    Birthday = datetime.strptime(date_str, "%Y-%m-%d")

    worksheet.write(row, col,     EmpID)
    worksheet.write(row, col + 1, Gender)
    worksheet.write(row, col + 1, Age)
    worksheet.write(row, col + 1, Sales)
    worksheet.write(row, col + 1, BMI)
    worksheet.write(row, col + 1, Salary)
    worksheet.write(row, col + 1, Birthday, date_format)
    row += 1

workbook.close()