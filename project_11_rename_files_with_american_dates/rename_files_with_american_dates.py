import os
import re
import shutil

os.chdir('project_11_rename_files_with_american_dates')

# Create a regex that can identify the text pattern of American-style dates.
US_date=re.compile(r'''
(\d{1,2}) # find 1 or 2 digits
- # find separator -
(\d{1,2})  # find 1 or 2 digits
- # find separator -
(\d{4}) # find exactly 4 digits
''',
re.VERBOSE)

# Call os.listdir() to find all the files in the working directory.
for filename in os.listdir(os.getcwd()):
# Loop over each filename, using the regex to check whether it has a date.
    mo=US_date.findall(filename)
    if len(mo)>0:
        # print(mo)
        # print(mo[0])
        month=str(mo[0][0])
        day=str(mo[0][1])
        year=str(mo[0][2])
# If it has a date, rename the file with shutil.move().
        data_tuple=(day, month, year)
        new_filename='report_' + ('-').join(data_tuple)
        new_filename+='.txt'
        shutil.move(filename,new_filename)