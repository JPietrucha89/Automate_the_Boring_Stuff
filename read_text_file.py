from pathlib import Path

file=open('.\os.txt')
text_string=file.read()
print(text_string)
file.close()

# nie dziala, nie mam pojecia czemu :P
p=Path(Path.cwd() / 'os.txt')
file=open(p)
print(file.readlines()) 
for line in file.readlines():
    print(line)

file.close()