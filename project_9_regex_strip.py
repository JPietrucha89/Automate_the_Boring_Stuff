#Regex Version of strip()
# Write a function that takes a string and does the same thing as the strip() string method.
# If no other arguments are passed other than the string to strip, then whitespace characters will be removed
# from the beginning and end of the string. Otherwise, the characters specified in the second argument to the
# function will be removed from the string.

import re

def regex_strip(text, text_to_strip=r'ABCDEFGHIJKLMNO'):
    if text_to_strip=='ABCDEFGHIJKLMNO':
        regex=re.compile(r"\s*([\w\d]+)\s*")
        mo=regex.findall(text)
        try:
            print(mo[0])
        except:
            print("Error")
    else:
        regex=re.compile(text_to_strip+"*([^"+text_to_strip+"]+)"+text_to_strip+"*")
        mo=regex.findall(text)
        try:
            separator=""
            print(separator.join(mo))
        except:
            print("Error")

def regex_strip_2(text, text_to_strip=r'ABCDEFGHIJKLMNO'):
    if text_to_strip=='ABCDEFGHIJKLMNO':
        regex=re.compile(r"\s*([\w\d]+)\s*")
        mo=regex.findall(text)
        try:
            print(mo[0])
        except:
            print("Error")
    else:
        regex=re.compile(r'[^'+text_to_strip+']+')
        mo=regex.findall(text)
        try:
            separator=""
            print(separator.join(mo))
        except:
            print("Error")

def regex_strip_3(text, text_to_strip=r'ABCDEFGHIJKLMNO'):
    if text_to_strip=='ABCDEFGHIJKLMNO':
        regex=re.compile(r"\s*([\w\d]+)\s*")
        mo=regex.findall(text)
        try:
            print(mo[0])
        except:
            print("Error")
    else:
        regex=re.compile(r'['+text_to_strip+']*')
        mo=regex.sub('',text)
        try:
            separator=""
            print(separator.join(mo))
        except:
            print("Error")
#main
print("Podaj tekst do stripowania")
text=input()

regex_strip(text)
regex_strip(text,"a")

regex_strip_2(text)
regex_strip_2(text,"a")

regex_strip_3(text)
regex_strip_3(text,"a")