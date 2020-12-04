f = open('input.txt').readlines()

firstline = f.pop(0)
pattern_size = len(firstline)
x_position = 0
position = (0, 0)
count = 0

for x in f:
    x_position += 3
    # position[0] += 3
    # position[1] += 1
    x_lookup = x_position % (pattern_size-1)
    print(x, x_lookup, x_position)
    if x[x_lookup] == "#":
        count += 1

print(count)