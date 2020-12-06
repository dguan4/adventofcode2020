f = open("input.txt")

values = []
count = 0

for x in f:
    if x == "\n":
        print(values, set(values))
        count += len(set(values))
        values = []
    else:
        for char in x.replace("\n", ""):
            values.append(char)

print(count)