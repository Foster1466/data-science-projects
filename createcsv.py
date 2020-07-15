# Run this code to create a dummy csv file to test task 1.1
import csv

with open('employee.csv', 'w', newline = '') as fp:
    a = csv.writer(fp, delimiter = ',')
    data = [['NAME', 'ID', 'LOCATION', 'Start_date', 'End_date', 'DOB', 'Date_of_promotion'],
            ['Jhonson', 'asr2000', 'Mumbai','19-06-2020','01-02-2025', '23-06-1995', '10-03-2022'],
            ['Rohan', 'asr2001', 'Thane','23-02-2020','02-05-2021', '04-04-1992', '12-03-2021'],
            ['Deepak', 'asr2002', 'Thane','16-06-2018','07-07-2024', '11-02-1995', '04-04-2023'],
            ['Aishwarya', 'asr2003', 'Mumbai','21-09-2017','11-12-2026', '20-06-1994', '06-08-2025'],
            ['Ajinkya', 'asr2004', 'Kalyan','16-11-2018','26-05-2023', '24-11-1995', '15-05-2022'],
            ['David', 'asr2005', 'Kalyan','13-02-2019','03-05-2027', '13-03-1996', '10-05-2024'],
            ['Sayili', 'asr2006', 'Thane','13-02-2020','05-06-2023', '08-12-1993', '12-05-2022']]
    a.writerows(data)
