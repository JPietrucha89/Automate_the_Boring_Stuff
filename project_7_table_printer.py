# Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each
#  column right-justified. Assume that all the inner lists will contain the same number of strings.
#  For example, the value could look like this:
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(listParameter):
    #zliczenie najdluzszego stringa w kazdej podliscie
    longestStringList=[0]*len(listParameter)
    for i in range(len(listParameter)):
        sublist=listParameter[i]
        longestStringSublist=0
        for index in range(len(sublist)):
            if len(sublist[index])>longestStringSublist:
                longestStringSublist=len(sublist[index])
                longestStringList[i]=longestStringSublist

    lenList=len(longestStringList)
    numberOfElementsInSublist=0
    for i in range(lenList):
        if len(listParameter[i])>numberOfElementsInSublist: numberOfElementsInSublist=len(listParameter[i])

    for i in range(numberOfElementsInSublist):
        print("")
        for index in range(lenList):
            #print(listParameter[index][i])
            print(listParameter[index][i].rjust(longestStringList[index]), end=" ")
#main
printTable(tableData)