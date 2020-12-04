f = open('input.txt')

dict = {}

for x in f:
    complement = 2020 - int(x)
    if complement in dict:
        print(x, complement, int(x) * complement)
    dict[int(x)] = 1