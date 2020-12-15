f = open('input.txt')

directionsL = ['E', 'N', 'W', 'S']
directionsR = ['E', 'S', 'W', 'N']

facing = 'E'
dict = {
    'N': 0,
    'S': 0,
    'E': 0,
    'W': 0
}
coord = (0, 0)

for x in f:
    instruction = x.strip()
    direction = instruction[0]
    # print(instruction[1:])
    # print(facing)
    if direction == 'F':
        dict[facing] += int(instruction[1:])
    elif direction == 'L':
        currDirection = directionsL.index(facing)
        angle = instruction[1:]
        getIndex = int(angle) * 4 // 360
        facing = directionsL[(currDirection + getIndex) % 4]
    elif direction == 'R':
        currDirection = directionsR.index(facing)
        angle = instruction[1:]
        getIndex = int(angle) * 4 // 360
        print(currDirection, angle, getIndex)
        facing = directionsR[(currDirection + getIndex) % 4]
    else:
        dict[direction] += int(instruction[1:])

print(dict)
print(dict['N'] - dict['S'], dict['E'] - dict['W'])
print(abs(dict['N'] - dict['S']) + abs(dict['E'] - dict['W']))