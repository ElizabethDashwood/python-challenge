# Import the os module to create file paths between operating systems
import os

# Module for reading CSV files
import csv

# Set file path to access csv file that is to be read for PyBank project
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Set steps to read the csv file using the CSV module defined previously
with open(csvpath) as csvfile:

    # Specify the variable that holds the csv file contents and the delimiter for the CSV file
    csvreader = csv.reader(csvfile, delimiter =',')
    print (csvreader)
    
    # Read the header row of the csv file using f-string
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

   # Count the number of data rows in the csv file
    csvcount = len(list(csvreader))
    # Reference: https://www.w3resource.com/python-exercises/modules/python-module-csv-exercise-2.php    
    # Reference:https://docs.python.org/3/tutorial/datastructures.html
    print("Total: " + str(csvcount))
    
   #Read each row of data after the header
    for row in csvreader:
       print(row)
    
          
    # Print Report Title
    print ("Financial Analysis")
    print ("----------------------------")
    print ("Total Months: " + str(csvcount))
    
    