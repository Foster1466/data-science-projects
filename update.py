# This code will create a column which will have the difference between the days of DOB and end-date. I couldn't figure out how to
# simultaneously create multiple columns, but i applied logic of difference in days in one column(created manually)
import pandas as pd
from dateutil.parser import parse
data = pd.read_csv("employee.csv")

# Store the values of number of rows and columns.
rows, columns = data.shape
#then use the loop to get value from each row of both columns
for i in range(rows):
    # Store value of end-date
    s = data.End_date[i]
    # Store value of date-of-birth
    e = data.DOB[i]
    # then use parser to convert these strings to date and subtract the days in them. So parse(s) will convert the string to
    # datetime object and the date() will return the date and subtract them and store in d
    d = parse(s).date() - parse(e).date()
    # then create a new column and keep on adding the calculated values to their respective rows.
    data.loc[i,'DOB-end_date'] = d
# and finally print the table
print(data)
