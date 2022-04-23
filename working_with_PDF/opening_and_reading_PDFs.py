import PyPDF2  # it cannot extract images or charts but it can extract text <it is something!>
import os
from pathlib import Path

pdfFile = open(Path(os.getcwd(), 'working_with_PDF',
               'meetingminutes.pdf'), 'rb')  # read binary
# create reader object by passing file object to PdfFileReader
reader = PyPDF2.PdfFileReader(pdfFile)

# numPages returns information about number of pages in PDF file
print(reader.numPages)

# if PDF file is protected by password/endrypted getPage() method will return error. It is advised to check if PDF is encrypted or not
print(reader.isEncrypted)
if reader.isEncrypted:
    reader.decrypt('password')  # decrypt/unprotect PDF file with password
page = reader.getPage(0)  # create page object
print(page.extractText())

# extract all text from PDF file
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

pdfFile.close
