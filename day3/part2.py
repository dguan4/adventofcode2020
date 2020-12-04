def findTrees(input_list, right, down, input_length):
    x_position = 0
    y_position = 0
    count = 0
    while y_position < len(input_list)-1:
        x_position += right
        y_position += down
        x_lookup = x_position % (input_length-1)
        print(y_position, x_lookup, len(input_list))
        if (input_list[y_position][x_lookup] == "#"):
            count += 1
    return count

f = open('input.txt')

# firstline = f.pop(0)
pattern_size = 0
input_list = []
count = 0

for x in f:
    input_list.append(x)
    pattern_size = len(x)

# print(input_list[0][2])
firstslope = findTrees(input_list, 1, 1, pattern_size)
secondslope = findTrees(input_list, 3, 1, pattern_size)
thirdslope = findTrees(input_list, 5, 1, pattern_size)
fourthslope = findTrees(input_list, 7, 1, pattern_size)
fifthslope = findTrees(input_list, 1, 2, pattern_size)
print(firstslope, secondslope, thirdslope, fourthslope, fifthslope)
print(firstslope*secondslope*thirdslope*fourthslope*fifthslope)

# for x in f:
#     x_position += 3
#     # position[0] += 3
#     # position[1] += 1
#     x_lookup = x_position % (pattern_size-1)
#     print(x, x_lookup, x_position)
#     if x[x_lookup] == "#":
#         count += 1