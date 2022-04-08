# SHELVE module
# Used to store data which is not plain text for example lists/dictionaries
import shelve
shelfFile=shelve.open('cat_list')
cats_list=['Rudy','Gruby','Leniwy']
shelfFile['cats']=cats_list
print(list(shelfFile.keys())) # ['cats']
print(list(shelfFile.values())) # ['Rudy','Gruby','Leniwy']
shelfFile.close()

# -----------------------------------------------
# pprint module can help with turning nonplain text data into plain text in order to save it into file for later use
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats)) #"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

""" And since Python scripts are themselves just text files with the .py file extension, your Python programs can even generate other Python programs. You can then import these files into scripts. """

import myCats
print(myCats.cats) # [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(myCats.cats[0]) # {'name': 'Zophie', 'desc': 'chubby'}
print(myCats.cats[0]['name']) # 'Zophie'