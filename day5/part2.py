import math

def doCalc(range, upper):
    """ upper is a bool which means to take upper bound """
    if upper:
        range = (math.ceil(range[0] + (range[1] - range[0])/2), range[1])
    else:
        range = (range[0], range[1] - math.ceil((range[1] - range[0])/2))
    return range

def getSeatRowAndColumn(x):
    row_column = [0, 0]
    col_range = (0, 7)
    range = (0, 127)
    for char in x:
        # print(range, char)
        if char == "F":
            if range[1] - range[0] == 1:
                row_column[0] = range[0]
            range = doCalc(range, False)
        elif char == "B":
            if range[1] - range[0] == 1:
                row_column[0] = range[1]
            range = doCalc(range, True)
        elif char == "R":
            if col_range[1] - col_range[0] == 1:
                row_column[1] = col_range[1]
            col_range = doCalc(col_range, True)
        elif char == "L":
            if col_range[1] - col_range[0] == 1:
                row_column[1] = col_range[0]
            col_range = doCalc(col_range, False)
    return row_column

f = open('input.txt')
highestCount = 0
ids = []
rowcolumndict = {}

for x in f:
    row_column = getSeatRowAndColumn(x)
    seatID = row_column[0] * 8 + row_column[1]
    rowcolumndict[seatID] = row_column
    ids.append(seatID)
    highestCount = max(highestCount, seatID)

ids.sort()
missing = [x for x in range(ids[0], ids[-1]) if x not in ids]
print(missing)
print(missing[0], rowcolumndict[missing[0]+1], rowcolumndict[missing[0]-1]) #figures out what column/row this missing id is
print(highestCount)