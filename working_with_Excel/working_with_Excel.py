import openpyxl
from pathlib import Path

file=Path(Path.cwd(),'working_with_Excel','example.xlsx')
# open individual excel file and create workbook object
wb=openpyxl.load_workbook(file)

# get names of sheets and values of cells
print(wb.sheetnames)
sheet=wb['Sheet1']
print(type(sheet))
print(sheet['A1'].value)
print(str(sheet['A1'].value))
print(sheet['B1'].value)
print(sheet['C1'].value)

# using .cell() method allows to pass columns name as number - useful for loops
print(sheet.cell(5,2).value)
for i in range(1,8):
    print(i,sheet.cell(i,2).value)

# create new worbook in memory
wb=openpyxl.Workbook()
print(wb.sheetnames) #defalut name of first sheet is Sheet
sheet=wb['Sheet']
sheet['A1'].value=10 # changing a cell's value is done using square brackets, just like changing values of list or dictionary
sheet['A2'].value='Python'
wb.save(Path(Path.cwd(),'working_with_Excel','new_workbook.xlsx'))

sheet2=wb.create_sheet() # add sheet with deafult name at the end of 
print(wb.sheetnames)
sheet2.title='My new sheet name' # rename sheet
print(wb.sheetnames)
wb.save(Path(Path.cwd(),'working_with_Excel','new_workbook_with_2_sheets.xlsx'))

sheet3=wb.create_sheet(index=0,title='My newest sheet name') # index allows to pick position of new worksheet - just like before/after:= in VBA
print(wb.sheetnames)
wb.save(Path(Path.cwd(),'working_with_Excel','new_workbook_with_3_sheets.xlsx'))