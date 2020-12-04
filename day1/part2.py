f = open('input.txt')

numlist = []

for x in f:
    numlist.append(int(x))

for i, num in enumerate(numlist, start=0):
    if i == len(numlist) - 2:
        break
    for j, num2 in enumerate(numlist, start=i+1):
        if (j == len(numlist) - 1):
            break
        for k, num3 in enumerate(numlist, start=j+1):
            if num+num2+num3 == 2020:
                print(num, num2, num3)
                print(num*num2*num3)