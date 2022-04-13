import shutil

# The shutil (or shell utilities) module has functions to let you copy, move, rename, and delete files in your Python programs.

# Calling shutil.copy(source, destination) will copy the file at the path source to the folder at the path destination. (Both source and destination can be strings or Path objects.) If destination is a filename, it will be used as the new name of the copied file. This function returns a string or Path object of the copied file.
# .copy() and copytree() can both be used for renaming
shutil.copy(source_path, destination_path)
shutil.copytree(source_path, destination_path)

# Calling shutil.copytree(source, destination) will copy the folder at the path source, along with all of its files and subfolders, to the folder at the path destination.
# same as .copy() and .copytree() - can be used for renaming
shutil.move(source_path, destination_path)