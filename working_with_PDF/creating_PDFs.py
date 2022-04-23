import PyPDF2  # it cannot extract images or charts but it can extract text <it is something!>
import os
from pathlib import Path

# PyPDF2 cannot write arbitrary text to a PDF like Python can do with plaintext files. Instead, PyPDF2’s PDF-writing capabilities are limited to copying pages from other PDFs, rotating pages, overlaying pages, and encrypting files. PyPDF2 doesn’t allow you to directly edit a PDF. Instead, you have to create a new PDF and then copy content over from an existing document.
# The examples in this section will follow this general approach:
# 1. Open one or more existing PDFs(the source PDFs) into PdfFileReader objects.
# 2. Create a new PdfFileWriter object.
# 3. Copy pages from the PdfFileReader objects into the PdfFileWriter object.
# 4. Finally, use the PdfFileWriter object to write the output PDF.

# JOIN TWO PDF FILES INTO NEW FILE
pdfFile = open(Path(os.getcwd(), 'working_with_PDF',
               'meetingminutes.pdf'), 'rb')  # read binary
# create reader object by passing file object to PdfFileReader
reader = PyPDF2.PdfFileReader(pdfFile)

pdfFile2 = open(Path(os.getcwd(), 'working_with_PDF',
                     'meetingminutes2.pdf'), 'rb')  # read binary
reader2 = PyPDF2.PdfFileReader(pdfFile2)

# Creating a PdfFileWriter object creates only a value that represents a PDF document in Python. It doesn’t create the actual PDF file. For that, you must call the PdfFileWriter’s write() method.
writer = PyPDF2.PdfFileWriter()  # create new, blank file
for pageNum in range(reader.numPages):
    pageObj = reader.getPage(pageNum)
    # optionally pages can be rotated by 90, 180, 270 degrees
    # pageObj.rotateClockwise(90)
    writer.addPage(pageObj)  # append page
for pageNum in range(reader2.numPages):
    pageObj = reader2.getPage(pageNum)
    writer.addPage(pageObj)  # append page
# NOTE
# PyPDF2 cannot insert pages in the middle of a PdfFileWriter object the addPage() method will only add pages to the end.

# The write() method takes a regular File object that has been opened in write-binary mode. You can get such a File object by calling Python’s open() function with two arguments: the string of what you want the PDF’s filename to be and 'wb' to indicate the file should be opened in write-binary mode.
outputFile = open(Path(os.getcwd(), 'working_with_PDF',
                       'combined_file.pdf'), 'wb')
# ENCRYPTING PDF
# PDFs can have a user password(allowing you to view the PDF) and an owner password(allowing you to set permissions for printing, commenting, extracting text, and other features). The user password and owner password are the first and second arguments to encrypt(), respectively. If only one string argument is passed to encrypt(), it will be used for both passwords.
writer.encrypt(user_pwd='user_pw', owner_pwd='owner_pw')
writer.write(outputFile)  # write out contents of writer object to output file
outputFile.close

# Overlaying Pages
# PyPDF2 can also overlay the contents of one page over another, which is useful for adding a logo, timestamp, or watermark to a page. With Python, it’s easy to add watermarks to multiple files and only to pages your program specifies.
minutesFirstPage = reader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
# merge allows to add timestamp or watermark to given minutesFirstPage
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, reader.numPages):
    pageObj = reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)

resultPdfFile.close
pdfFile.close
pdfFile2.close
