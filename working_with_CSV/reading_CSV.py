# Each line in a CSV file represents a row in the spreadsheet, and commas separate the cells in the row.

# reader Objects
# To read data from a CSV file with the csv module, you need to create a reader object. A reader object lets you iterate over lines in the CSV file.

import csv
import os
from pathlib import Path

exampleFile = open(Path(os.getcwd(), 'working_with_CSV', 'example.csv'))
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)  # get all rows/cells into the list
print(exampleData)
print()
print(exampleData[0])  # print just first row

# The reader object can be looped over only once. To reread the CSV file, you must call csv.reader to create a reader object.
print()
exampleFile = open(Path(os.getcwd(), 'working_with_CSV', 'example.csv'))
exampleReader = csv.reader(exampleFile)
# Showing all *.csv files contents in a prettier way
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

# IF CSV FILE HAS HEADERS IT IS BETTER TO USE DICTREADER INSTEAD OF READER
# Inside the loop, DictReader object sets row to a dictionary object with keys derived from the headers in the first row.

print()
exampleFile = open(
    Path(os.getcwd(), 'working_with_CSV', 'exampleWithHeader.csv'))
exampleDictReader = csv.DictReader(exampleFile)
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
