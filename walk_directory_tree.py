# use os.walktree() to loop through all folder, subfolders and files in given directory
import os

folder_path='D:\Filmy'

print(os.walk(folder_path))

for folder_name, subfolders, filenames in os.walk(folder_path):
    print(folder_name)
    print(subfolders) # list of subfolders
    print(filenames) # list of files in current folder
    print() # print newline for better readabilty