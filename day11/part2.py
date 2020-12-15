from copy import deepcopy

f = open("input.txt")
input = [list(x.strip()) for x in f]

def checkInput(x, y, xChange, yChange):
    newX = x+xChange
    newY = y+yChange
    if newX < 0 or newX >= len(input[0]) or newY >= len(input) or newY < 0:
        return True
    else:
        if input[newY][newX] == "#":
            return False
        elif input[newY][newX] == ".":
            return checkInput(newX, newY, xChange, yChange)
        else:
            return True

# def checkInputsForAll(x, y):
#     if input[y][x] == ".":
#         return False
#     return (checkInput(x, y, -1, -1) #top left
#      and checkInput(x, y, 0, -1) #top 
#      and checkInput(x, y, 1, -1) #top right
#      and checkInput(x, y, 1, 0) #right
#      and checkInput(x, y, 1, 1) #bottom right
#      and checkInput(x, y, 0, 1) #bottom
#      and checkInput(x, y, -1, 1) #bottom left
#      and checkInput(x-1, y, -1, 0)) #left  

def checkInputsForCount(x, y):
    if input[y][x] == ".":
        return 10
    count = 0
    if not checkInput(x, y, -1, -1): #top left
        count += 1
    if not checkInput(x, y, 0, -1): #top 
        count += 1
    if not checkInput(x, y, 1, -1): #top right
        count += 1
    if not checkInput(x, y, 1, 0): #right
        count += 1
    if not checkInput(x, y, 1, 1): #bottom right
        count += 1
    if not checkInput(x, y, 0, 1): #bottom
        count += 1
    if not checkInput(x, y, -1, 1): #bottom left
        count += 1
    if not checkInput(x, y, -1, 0): #left  
        count += 1
    return count

def checkAdjacent():
    ans = deepcopy(input)
    for y in range(len(input)):
        for x in range(len(input[y])):
            checkCount = checkInputsForCount(x, y)
            if checkCount == 0:
                ans[y][x] = "#"
            elif ans[y][x] == "#" and checkCount >= 5:
                ans[y][x] = "L"
    return ans

answer = []
iterations = 0
while answer != input:
    iterations += 1
    answer = deepcopy(input)
    input = checkAdjacent()


print(answer, iterations, sum(sublist.count("#") for sublist in answer))