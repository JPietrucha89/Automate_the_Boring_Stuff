import random
from datetime import date
import os

number_of_files=10
current_date=date.today()
current_year=current_date.year

os.chdir('project_11_rename_files_with_american_dates')

for i in range(10):
    month=random.randint(1,12)
    year=random.randint(1900,current_year)
    if month in (1, 3, 5, 7, 8, 10, 12):
        day=random.randint(1,31)
    elif month in (4, 6, 9, 11):
        day=random.randint(1,30)
    else:
        day=random.randint(1,28)
    data_tuple=(str(month),str(day),str(year))
    filename=('-').join(data_tuple)
    # create file with randomized name
    open('report_' + filename + '.txt', 'w') 