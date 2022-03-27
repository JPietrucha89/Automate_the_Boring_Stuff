import re

#metoda FINDALL znajduje WSZYSTKIE pasujace ciagi znakow i zwraca je w postaci listy
PhoneRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=PhoneRegex.search('123-456-7890 098-765-4321')
print(mo.group())

mo2=PhoneRegex.findall('123-456-7890 098-765-4321')
print(mo2) #tutaj zwrocona zostaje lista wszystkich znalezionych ciagow znakow, ktore pasuja do klucza


PhoneRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo3=PhoneRegex.findall('123-456-7890 098-765-4321')
print(mo3) #tutaj zwrocona zostaje lista skladajaca sie z tupli, dzieje sie tak ze wzgledu na grupowanie () w .COMPILE

#utworzenie wlasnego Character Class
vowelRegex=re.compile(r'[aeiouAEIOU]')
mo4=vowelRegex.findall('Liczy sie przyszlosc pokolen')
print(mo4)

# symbol ^ wyszukuje wszystkie symbole OPROCZ tych podanych w nawiasie kwadratowym w metodzie .COMPILE
vowelRegex=re.compile(r'[^aeiouAEIOU]')
mo5=vowelRegex.findall('Liczy sie przyszlosc pokolen')
print(mo5)