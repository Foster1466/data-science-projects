# This code will check each column for a specific pattern to figure out which column has address and if found then use that column
# to extract the zipcode from each row and create a new column which will have the extracted zipcodes(only the first 5 digits).
import pandas as pd

# Creating a dummy dataframe to work on.
d = {'name':['bob','john'],'address':['123 6th Street,Sterling VA 20165-7513','567 7th Street, Wilmington NC 40361']}
df = pd.DataFrame(d)

print("Original Table: ")
print(df)
print()
print()

# This function will check for address.
def checkcolumn(column):
    # For every value in column:
    for d in column:
        # I noticed that most of the american address starts with a 3 digit number. So i stored the first 3 letters of d to check
        # weather those 3 letters can be converted to integers or not. If yes then the given string is an address
        ele = d[0:3]
        try:
            int(ele)
            return True
        except:
            return False

# A list variable that stores all the columns of a table. To test out the logic with a random dataset just write the names of each
# column in this list.
list = [df['name'],df['address']]
temp = 1
# Similar to task 1.1 this loop will also take each column of the dataset from list and check which column has address
for i in list:
    # So send a column and if True print out which column has address
    if checkcolumn(i):
        print("Column ", temp, " has address")
    temp += 1

print();print()
# After figuring out which column has address. Store the rows of that column in a list to get the zipcodes
address = list[temp-2].tolist()
# For each value in the list
for i in range(len(address)):
    # Split a string into a list where each word is a list item. String is split using space as a separator
    data = address[i].split(' ')
    ''' Since the zipcodes are usually written at the end of the address. reverse the list and store the 1st value of that list
    in a variable'''
    code = data[::-1][0]
    ''' Now check weather that value can be converted to integer. If yes then store that value in variable check and create a new
    column and add that value to the respective row. This will make sure only first 5 digits are being extracted from zipcode.'''
    try:
        check = int(code[0:5])
        if isinstance(check, int):
            df.loc[i,'Zip code'] = code[0:5]
    # If any error occurs then it means that the address does not contain zipcode and we will just add a NaN value as input(application of imputation).
    except:
        df.loc[i,'Zip code'] = 'NaN'
print(df)
