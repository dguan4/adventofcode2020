f = open('input.txt')

def getAccumulator(instructions):
    current_instruction = 0
    val = 0
    instruction_visited = [False]*len(instructions)

    while current_instruction < len(instructions) and instruction_visited[current_instruction] == False:
        instruction = instructions[current_instruction]
        instruction_visited[current_instruction] += 1
        if instruction[0] == "acc":
            val += instruction[1]
            current_instruction += 1
        elif instruction[0] == "jmp":
            current_instruction += instruction[1]
        else:
            current_instruction += 1
    
    print("get accumulator", val, current_instruction, current_instruction == len(instructions))
    return (val, current_instruction)

instructions = []

for x in f:
    split_line = x.split(" ")
    instructions.append([split_line[0], int(split_line[1])])

global_val = 0
global_instruction = 0

for index, instruction in enumerate(instructions):
    curr_instr = instruction[0]
    if curr_instr == "jmp" or curr_instr == "nop":
        if curr_instr == "jmp":
            instructions[index][0] = "nop"
            # print(curr_instr, instructions)
        elif curr_instr == "nop":
            instructions[index][0] = "jmp"
            # print(curr_instr, instructions)
        (global_val, global_instruction) = getAccumulator(instructions)
        # print(global_val, global_instruction, len(instructions))
        if global_instruction == len(instructions):
            break
        else:
            # print(curr_instr)
            instructions[index][0] = curr_instr
    
# val, program_ended_successfully = getAccumulator(instructions)
    
print(global_val, global_instruction)
