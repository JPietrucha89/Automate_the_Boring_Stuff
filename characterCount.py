import pprint #modul pprint pozwala ladniej wydrukowac zawartosc listy albo slownika

message="It was a bright cold day in April, and the clocks were striking thirteen"
count={}

for i in range(len(message)):
    character=message[i].lower()

    count.setdefault(character,0)
    count[character]=count[character]+1

pprint.pprint(count)