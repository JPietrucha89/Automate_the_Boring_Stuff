# gra w ktorej gracz probuje zgadnac liczbe wylosowana przez program
# przedzial liczbowy <1,20>
# liczba prob - 7
import random

def wylosujLiczbe():
    return random.randint(1,20)

#main
limitProb=7
licznikProb=0
wylosowanaLiczba=wylosujLiczbe()

print(wylosowanaLiczba)

print("Witaj graczu, podaj swoje imie :)")

try:
    imieGracza=input()
except:
    print("Nie podales imienia trollu!")
    SystemExit

print("Czesc "+ imieGracza+ ", podaj liczbe.")

while licznikProb<limitProb:
    try:
        podanaLiczba=int(input())
    except:
        print("Nalezy podac liczbe!")
        continue

    if podanaLiczba<wylosowanaLiczba:
        print("Podana przez Ciebie liczba jest za mala. Probuj dalej :) Liczba pozostalych prob wynosi: ",limitProb-licznikProb)
    elif podanaLiczba>wylosowanaLiczba:
        print("Podana przez Ciebie liczba jest za duza. Probuj dalej :) Liczba pozostalych prob wynosi: ",limitProb-licznikProb)
    else:
        print("Udalo Ci sie zgadnac, brawo! Wylosowana liczba to ", wylosowanaLiczba)
        break
    licznikProb=licznikProb+1

if licznikProb>=limitProb:
    print("Przykro mi, ", imieGracza," nie udalo Ci sie zgadnac :( Wylosowana liczba wynosila ", wylosowanaLiczba )