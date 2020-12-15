f = open('input.txt')

coord = [0, 0]
waypoint = [10, 1] # east and north are positive

for x in f:
    instruction = x.strip()
    direction = instruction[0]
    movement = int(instruction[1:])
    if direction == 'F':
        diffX = waypoint[0]*movement
        diffY = waypoint[1]*movement
        coord[0] += diffX
        coord[1] += diffY
        # waypoint[0] += diffX
        # waypoint[1] += diffY
    elif direction == 'L': 
        # assuming ship is (0, 0); if waypoint is (10, 0)
        # then waypoint becomes (0, 10), (-10, 0), (0, -10), (10, 0), etc
        for rotate in range(movement//90):
            waypoint[0],waypoint[1] = -waypoint[1],waypoint[0]
    elif direction == 'R':
        # assuming ship is (0, 0); if waypoint is (10, 0)
        # then waypoint becomes (0, -10), (-10, 0), (0, 10), (10, 0), etc
        for rotate in range(movement//90):
            waypoint[0],waypoint[1] = waypoint[1],-waypoint[0]
    elif direction == 'E':
        waypoint[0] += movement
    elif direction == 'N':
        waypoint[1] += movement
    elif direction == 'W':
        waypoint[0] -= movement
    elif direction == 'S':
        waypoint[1] -= movement

print(waypoint, coord)
print(sum([abs(x) for x in coord]))