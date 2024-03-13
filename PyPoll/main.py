# Import the os module to create file paths between operating systems
import os

# Module for reading CSV files
import csv

# Set file path to access csv file that is to be read
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Set steps to read csv file using the CSV module defined previously
with open(csvpath) as csvfile:

    # Specify the variable that holds the csv file contents and the delimiter for the CSV file
    csvreader = csv.reader(csvfile, delimiter = ',')
    print (csvreader)

    # Read the header row of the csv file and print using f-string
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
