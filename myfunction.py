#This code will check every single value in the table and will finally tell which columns contain date
import pandas as pd
# Parser module offers a generic date/time string parser which is able to parse most known formats to represent a date and/or time
from dateutil.parser import parse

def isdate(string, fuzzy=False):
    # For each value check weather the given string can be converted to represent a date
    try:
        # if string can be converted to date return true
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        # if not then error occurs so return false
        return False

data = pd.read_csv('employee.csv')

#This function identifies which column has date
def checkcolumn(column):
    # Initially we consider a column does not have date
    dateavailable = 0
    # Usinf loop to check each value in column
    for d in column:
        # if function returns true then atleast one given value from a column is date.
        if isdate(d):
            # so change the value of variable to 1 and return true
            dateavailable = 1
            return True
    # If a column does not have date then the value of dateavailable == 0 so it will return false
    if dateavailable != 1:
        return False

# A list variable that stores all the columns of a table. To test out the logic with a random dataset just write the names of each
# column in this list.
list = [data['NAME'],data['ID'],data['LOCATION'],data['Start_date'],  data['End_date'],  data['DOB'], data['Date_of_promotion']]
temp = 1
#This loop will take each column of a dataset from the list and check which column has date
for i in list:
    # check weather each column has a date or not. If yes then print the column number as the output
    if checkcolumn(i):
        print("Column ", temp, "has date")
    temp += 1
