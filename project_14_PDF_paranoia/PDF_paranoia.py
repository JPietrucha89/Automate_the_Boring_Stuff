import os
import PyPDF2
from pathlib import Path

test_path = Path(os.getcwd(), 'project_14_pdf_paranoia', 'test_folder')


# Using the os.walk() function from Chapter 10, write a script that will go through every PDF in a folder (and its subfolders) and encrypt the PDFs using a password provided on the command line. Save each encrypted PDF with an _encrypted.pdf suffix added to the original filename. Before deleting the original file, have the program attempt to read and decrypt the file to ensure that it was encrypted correctly.
def encrypt_PDFs(path, encryption_password):
    for folder_name, subfolders, filenames in os.walk(path):
        print(folder_name)
        print(subfolders)  # list of subfolders
        print(filenames)  # list of files in current folder
        print()  # print newline for better readabilty
        for pdf in filenames:
            if not "_encrypted" in pdf:
                pdfFile = open(Path(folder_name, pdf), 'rb')
                reader = PyPDF2.PdfFileReader(pdfFile)
                if reader.isEncrypted == False:
                    outputFile = open(
                        Path(folder_name, pdf.split(".")[0]+'_encrypted.pdf'), 'wb')
                    writer = PyPDF2.PdfFileWriter()
                    for i in range(reader.getNumPages()):
                        pageObj = reader.getPage(i)
                        writer.addPage(pageObj)
                    writer.encrypt(encryption_password)
                    writer.write(outputFile)
    pass

# Then, write a program that finds all encrypted PDFs in a folder (and its subfolders) and creates a decrypted copy of the PDF using a provided password. If the password is incorrect, the program should print a message to the user and continue to the next PDF.


def decrypt_PDFs(path, decryption_password):
    for folder_name, subfolders, filenames in os.walk(path):
        print(folder_name)
        print(subfolders)  # list of subfolders
        print(filenames)  # list of files in current folder
        print()  # print newline for better readabilty
        for pdf in filenames:
            if "_encrypted" in pdf:
                pdfFile = open(Path(folder_name, pdf), 'rb')
                reader = PyPDF2.PdfFileReader(pdfFile)
                if reader.isEncrypted:
                    reader.decrypt(decryption_password)
                    outputFile = open(
                        Path(folder_name, pdf.split(".")[0]+'_decrypted.pdf'), 'wb')
                    writer = PyPDF2.PdfFileWriter()
                    for i in range(reader.getNumPages()):
                        pageObj = reader.getPage(i)
                        writer.addPage(pageObj)
                    writer.write(outputFile)
    pass


# main
encrypt_PDFs(test_path, 'Muszyna')

decrypt_PDFs(test_path, 'Muszyna')
