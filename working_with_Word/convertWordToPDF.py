# Code to create Word document goes here. comment with docx function calls to create your own content for the PDF in a Word document.
# To write a program that produces PDFs with your own content, you must use the docx module to create a Word document, then use the Pywin32 package’s win32com.client module to convert it to a PDF. Replace the
import win32com.client  # install with "pip install pywin32==224"
import docx

wordFilename = 'your_word_document.docx'
pdfFilename = 'your_pdf_filename.pdf'

doc = docx.Document()
# Code to create Word document goes here.
doc.save(wordFilename)

wdFormatPDF = 17  # Word's numeric code for PDFs.
wordObj = win32com.client.Dispatch('Word.Application')

docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
docObj.Close()
wordObj.Quit()
