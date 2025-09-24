tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    biggestItem = 0
    colWidth = []
    #These loops will assign the numeric value of the longest strings to colWidth
    for col in tableData: #grabs the list inside the outterlists
        for item in col: #grabs each item from the innerlist
            if len(item) > biggestItem: #Compares the length of the current item against the prior longest string
                biggestItem = len(item) #It is longer, assigns biggestItem to the new longest, basically max function.
        
        colWidth.append(biggestItem) #adds the biggestItem from this column to colWidth
        biggestItem = 0 #reset for next column

    #These loops will now format the columns and print
    for a in range(len(tableData[0])): #equivalent to '4' because list 0 in list tableData has 4 items.
        vertTable = [] #empty table to hold a column at a time
        for b in range(len(tableData)): #equivalent to '3' because list tableData has 3 items.
            item = tableData[b][a].rjust(colWidth[b]) #takes an item and adds spacing relavant to the column, to the right of each entry.
            vertTable.append(item) #adds the newly spaced item to the table.
        print(' '.join(vertTable)) #Adds spacing between each entry and prints the item.

printTable()