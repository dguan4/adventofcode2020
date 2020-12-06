f = open('sample.txt')

group_count = 0
overall_count = 0
values = []

for x in f:
    if x == "\n":
        test = [x for x in values if values.count(x) == group_count]
        print(test)
        overall_count += len(set(test))
        group_count = 0
        values = []
    else:
        group_count += 1
        for char in x.replace("\n", ""):
            values.append(char)

print(overall_count)