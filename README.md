# data-science-projects

Files in this projects use pandas library as primary resource that helps to interact with tabular data. 
Each file is well commented so that it is easy to find out what is happening.
A short description of each file:
1. createcsv.py: This file will create a dummy csv file that is used in myfunction.py
2. myfunction.py: This code will check every single value in the table and will finally tell which columns contain date
3. update.py: This code will create a column which will have the difference between the days of DOB and end-date.
4. zipcode.py: This code will check each column for a specific pattern to figure out which column has address and if found then use that column to extract the zipcode from each row and create a new column which will have the extracted zipcodes(only the first 5 digits).
5. typos.py: This code will check the column which has names in it and verify if the first letter of that name is capital or not. If not then it update that value.

It is recommended to follow the above pattern to check the work done.
