import csv
import os
from pathlib import Path

# creater File object and pass it to writer
outputFile = open(Path(os.getcwd(), 'working_with_CSV',
                  'output.csv'), 'w', newline='')
writer = csv.writer(outputFile)

# write rows into writer object
writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
writer.writerow([1, 2, 3.141592, 4])

outputFile.close()

# Or use DictWriter to create CSV files with headers
outputFile = open(Path(os.getcwd(), 'working_with_CSV',
                  'outputWithHeaders.csv'), 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])

# If you want your file to contain a header row, write that row by calling writeheader(). Otherwise, skip calling writeheader() to omit a header row from the file.
outputDictWriter.writeheader()

# You then write each row of the CSV file with a writerow() method call, passing a dictionary that uses the headers as keys and contains the data to write to the file.
# Notice that the order of the key-value pairs in the dictionaries you passed to writerow() doesn’t matter: they’re written in the order of the keys given to DictWriter(). Notice also that any missing keys, such as 'Pet' in {'Name': 'Bob', 'Phone': '555-9999'}, will simply be empty in the CSV file.
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})

outputFile.close()
