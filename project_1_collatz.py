def collatz(number):
    if number%2==0:
        return number//2
    else:
        return 3*number+1

#main
while True:
    print("Podaj liczbe")
    try:
        liczba=int(input())
        break
    except:
        print("Nie podales liczby!")

while liczba>1:
    print(collatz(liczba))
    liczba=collatz(liczba)