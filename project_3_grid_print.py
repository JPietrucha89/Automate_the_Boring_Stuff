#Copy the previous grid value, and write code that uses it to print the image.
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

szerokosc=len(grid)
wysokosc=len(grid[0])

#najpierw petla po indeksie kolumny, potem petla po indeksie wiersza
for i in range(wysokosc):
    for x in range(szerokosc):
        print(grid[x][i],end="")
        if x==szerokosc-1: #jesli to ostatni element kolumny to nalezy wydrukowac newLine
            print()
