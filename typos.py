# This code will check the column which has names in it and verify if the first letter of that name is capital or not. If not then it
# update that value.
import pandas as pd

# Same dummy dataset used in previous 5.1 task.
d = {'name':['bob','john'],'address':['123 6th Street,Sterling VA 20165-7513','567 7th Street, Wilmington NC 40361']}
df = pd.DataFrame(d)
print("Original dataframe: ")
print(df)
print()

# Function will check if a column has name or not
def checkcolumn(column):
    # For every value in column. Since name column will only contain alphabets and nothing else
    for d in column:
        string = str(d)
        # If the value is alphanumeric, meaning if string does not contain any numbers. then the string is a name.
        if string.isalpha():
            ans = True
        else:
            return False
    return ans
''' A list variable that stores all the columns of a table. To test out the logic with a random dataset just write the names of each
    column in this list.
'''
list = [df['name'], df['address']]
temp = 1
for i in list:
    # if true then print the column number.
    if checkcolumn(i):
        print("Column ", temp, " has name")
        break
    temp += 1

'''Now we will check if the first letter of each name in name column is capital or not'''
# Store the values of name column in a list.
name = list[temp-1].tolist()
# For each name:
for i in name:
    # check which values have names starting with lower cap letter
    if i.istitle() != True:
        # Then replace that name starting with a capital letter using replace function
        df.replace(to_replace = i, value = i.title(), inplace = True)

print()
# print updated table.
print ('After operation')
print(df)
