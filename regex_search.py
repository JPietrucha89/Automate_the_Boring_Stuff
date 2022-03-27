import re

#metoda search znajduje PIERWSZY pasujacy ciag znakow

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

#grupowanie
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex.search('My number is 415-555-4242.')
print(mo2.group(1))
print(mo2.group(2))
print(mo2.group(0))
print(mo2.group())

areaCode, mainNumber = mo2.groups()
print(areaCode)
print(mainNumber)

# symbol ? oznacza "jeden raz lub wcale"
batRegex=re.compile(r'Bat(wo)?man') # ? 
mo=batRegex.search("The Adventures of Batwoman")
print(mo.group())

# symbol * oznacza "zero razy lub wiecej"
batRegex=re.compile(r'Bat(wo)*man') # *
mo=batRegex.search("The Adventures of Batwowowowoman")
print(mo.group())

# symbol + oznacza "jeden raz lub wiecej"
batRegex=re.compile(r'Bat(wo)+man') # *
mo=batRegex.search("The Adventures of Batwowowoman")
print(mo.group())

# escaping \
regex=re.compile(r'\+\*\?')
mo=regex.search('I learned about +*? regex syntax')
print(mo.group())

# {X} szuka wyrazenia wystepujacego X razy pod rzad
haRegex=re.compile(r'(Ha){3}')
mo=haRegex.search('He said "HaHaHa"')
print(mo.group())

# {X,Y} szuka wyrazenia wystepujacego od X do Y razy pod rzad
haRegex=re.compile(r'(Ha){3,5}')
mo=haRegex.search('He said "HaHaHaHaHa"')
print(mo.group())

#greedy and nongreedy matches
digitRegex=re.compile(r'(\d){3,}') #pozostawienie prawego argumentu pustego oznacza "szuka od 3 az do nieskonczonosci"
mo=digitRegex.search("1234567890")
print(mo.group())
digitRegex=re.compile(r'(\d){3,5}?') #? nongreedy match czyli szuka mozliwie najkrotszego ciagu
mo=digitRegex.search("1234567890")
print(mo.group())