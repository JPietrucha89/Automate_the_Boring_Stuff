#Strong Password Detection
#Write a function that uses regular expressions to make sure the password string it is passed is strong. 
# A strong password is defined as one that is at least eight characters long, contains both uppercase and
#  lowercase characters, and has at least one digit. You may need to test the string
#  against multiple regex patterns to validate its strength.
import re

def check_length_8(password):
    regex=re.compile(r'.+')
    mo=regex.findall(password)
    try:
        if len(mo[0])>=8: 
            return True
        else:
            print("Haslo za krotkie!")
            return False
    except:
        print("Haslo za krotkie!")
        return False

def check_uppercase(password):
    regex=re.compile(r'[A-Z]+')
    mo=regex.findall(password)
    try:
        if len(mo[0])>=1: 
            return True
        else:
            print("Brak uppercase!")
            return False
    except:
        print("Brak uppercase!")
        return False

def check_lowercase(password):
    regex=re.compile(r'[a-z]+')
    mo=regex.findall(password)
    try:
        if len(mo[0])>=1: 
            return True
        else:
            print("Brak lowercase!")
            return False
    except:
        print("Brak lowercase!")
        return False

def check_digit(password):
    regex=re.compile(r'\d+')
    mo=regex.findall(password)
    try:
        if len(mo[0])>=1: 
            return True
        else:
            print("Brak cyfry!")
            return False
    except:
        print("Brak cyfry!")
        return False
#main
print("Podaj haslo. Musi zawierac 8 znakow, przynajmniej jeden uppercase, przynajmniej jeden lowercase i przynajmniej jedna cyfre.")
password=input()

if check_length_8(password) and check_uppercase(password) and check_lowercase(password) and check_digit(password):
    print("Porzadne haslo!")