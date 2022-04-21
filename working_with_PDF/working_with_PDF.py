import PyPDF2  # it cannot extract images or charts but it can extract text <it is something!>
import os
from pathlib import Path

pdfFile = open(Path(os.getcwd(), 'working_with_PDF',
               'meetingminutes.pdf'), 'rb')  # read binary
# create reader object by passing file object to PdfFileReader
reader = PyPDF2.PdfFileReader(pdfFile)

# numPages returns information about number of pages in PDF file
print(reader.numPages)
page = reader.getPage(0)  # create page object
print(page.extractText())

# extract all text from PDF file
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

# JOIN TWO PDF FILES INTO NEW FILE
pdfFile2 = open(Path(os.getcwd(), 'working_with_PDF',
                     'meetingminutes2.pdf'), 'rb')  # read binary
reader2 = PyPDF2.PdfFileReader(pdfFile2)

writer = PyPDF2.PdfFileWriter()  # create new, blank file
for pageNum in range(reader.numPages):
    writer.addPage(reader.getPage(pageNum))  # append page
for pageNum in range(reader2.numPages):
    writer.addPage(reader2.getPage(pageNum))  # append page

outputFile = open(Path(os.getcwd(), 'working_with_PDF',
                       'combined_file.pdf'), 'wb')
writer.write(outputFile)  # write out contents of writer object to output file
outputFile.close
pdfFile.close
pdfFile2.close
