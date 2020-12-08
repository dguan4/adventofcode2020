f = open('input.txt')

current_instruction = 0
global_val = 0
instructions = []
instruction_visited = []

for x in f:
    split_line = x.split(" ")
    instructions.append([split_line[0], int(split_line[1])])

instruction_visited = [0]*len(instructions)

while current_instruction < len(instructions):
    if instruction_visited[current_instruction] == True:
        break
    print(current_instruction, instruction_visited, instructions)
    instruction = instructions[current_instruction]
    instruction_visited[current_instruction] += 1
    if instruction[0] == "acc":
        global_val += instruction[1]
        current_instruction += 1
    elif instruction[0] == "jmp":
        current_instruction += instruction[1]
    else:
        current_instruction += 1
    
print(global_val)
