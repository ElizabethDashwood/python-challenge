# python-challenge
Description: This is the Module 3 Homework Challenge for Python scripting

Getting started: This challenge has 2 projects called:
  1. PyBank using a starter code csv file called budget_data.csv
  2. PyPoll using a started code csv file called election data.csv

Installations required:
  These projects have been run in a Windows 11 GitBash environment, using Python 3.10.13 together with Visual Studio Code Version 1.87.2 as the editor

Executing Homework Challenge Requirements: 

Please see python-challenge/PyBank/main.py for the script which performs the following 2 steps:

**Step 1: Correctly Reads in the CSV**
For PyBank project, the main.py python script file under 'python-challenge/PyBank' runs the process of reading the csv file and storing the header row.
The script and output are as follows:

**When the script runs for the command line in python using the python main.py command, the output shows the csv header:**
$ python main.py
<_csv.reader object at 0x000001CD7C135EA0>
CSV Header: ['Date', 'Profit/Losses']

**Step 2: Correctly determines the number of records in the csv file using len() and list functions**
**When the script runs for the command line in python using the python main.py command, the output shows the total number of months**
Total: 86



# Import the os module to create file paths between operating systems
import os

# Module for reading CSV files
import csv

# Set file path to access csv file that is to be read
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Set steps to read the csv file using the CSV module defined previously
with open(csvpath) as csvfile:

    # Specify the variable that holds the csv file contents and the delimiter for the CSV file
    csvreader = csv.reader(csvfile, delimiter =',')
    print (csvreader)

    # Read the header row of the csv file using f-string
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")



For PyPoll project, the main.py python script file under 'python-challenge/PyPoll' runs the process of reading the csv file and storing the header row.
The script and output are as follows:

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

**When the script runs for the command line in python using the python main.py command, the output shows the csv header:**



$ python main.py
<_csv.reader object at 0x00000198B1305DE0>
CSV Header: ['Ballot ID', 'County', 'Candidate']

**Step 2: Correctly determines the number of records in the csv file using len() and list fucntions**
# Count the number of data rows in the csv file
    csvcount = len(list(csvreader))
    # Reference: https://www.w3resource.com/python-exercises/modules/python-module-csv-exercise-2.php    
    # Reference:https://docs.python.org/3/tutorial/datastructures.html
    print("Total: " + str(csvcount))

Total: 369711
