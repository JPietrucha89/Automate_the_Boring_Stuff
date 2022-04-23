# At a high level, here’s what the program will do:

# Find all PDF files in the current working directory.
# Sort the filenames so the PDFs are added in order.
# Write each page, excluding the first page, of each PDF to the output file.

import os
import PyPDF2
from pathlib import Path

# Find all PDF files in the current working directory.
files_list = os.listdir(Path(os.getcwd(), 'working_with_PDF'))
pdfs_list = []

for file in files_list:
    if '.pdf' in file:
        if 'meetingminutes' in file:
            pdfs_list.append(file)

pdfs_list.sort()
print(pdfs_list)

writer = PyPDF2.PdfFileWriter()

for pdf in pdfs_list:
    pdfFile = open(Path(os.getcwd(), 'working_with_PDF', pdf), 'rb')
    reader = PyPDF2.PdfFileReader(pdfFile)
    for page in range(1, reader.numPages):
        pageObj = reader.getPage(page)
        writer.addPage(pageObj)

outputFile = open(
    Path(os.getcwd(), 'working_with_PDF', 'all_minutes.pdf'), 'wb')
writer.write(outputFile)
outputFile.close()
pdfFile.close()
