import re

# symbol ^ oznacza, ze przeszukiwany ciag MUSI ZACZYNAC sie od podanej frazy
beginsWithHelloRegex=re.compile(r'^Hello')
mo=beginsWithHelloRegex.search("Hello there")
print(mo.group())

# symbol $ oznacza, ze przeszukiwany ciag MUSI KONCZYC sie od podana frazas
beginsWithHelloRegex=re.compile(r'world!$')
mo2=beginsWithHelloRegex.search("Hello world!")
print(mo2.group())

allDigitsRegex=re.compile(r'^\d+$') # ciag znakow ZACZYNA sie i KONCZY cyframi, w dodtku w srodku moga byc tylko cyfry
mo3=allDigitsRegex.search("123456")
mo4=allDigitsRegex.search("123b56") # tutaj wkradla sie litera wiec .search zwroci None

print(mo3.group())
print(mo4)

# symbol . oznacza wildcard czyli dowolny jeden symbol
atRegex=re.compile(r'.{1,2}at')
mo5=atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo5)

string="Pierwsze imie: Jakub Nazwisko: Pietrucha"
nameRegex=re.compile(r":.(\w+)")
mo6=nameRegex.findall(string)
print(mo6)

# porownanie greedy i nongreedy
serve= '<To serve humans> for dinner>'
nongreedy=re.compile(r'<(.+?)>')
greedy=re.compile(r'<(.+)>')

mo_nongreedy=nongreedy.findall(serve)
mo_greedy=greedy.findall(serve)

print('Nongreedy matching: ',mo_nongreedy[0])
print('Greedy matching: ', mo_greedy[0])

prime="Serve the public trust. \nProtect the innocent. \nUpload the law."
dotStar=re.compile(r'.+')
mo7=dotStar.findall(prime)
print(mo7)