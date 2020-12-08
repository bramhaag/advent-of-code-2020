def as_instruction(line):
    opcode, value = line.split(" ")
    return (opcode, int(value))

def run(instructions):
    instruction_pointer = 0
    accumulator = 0

    visited = set([])

    while instruction_pointer < len(instructions):
        opcode, value = instructions[instruction_pointer]
        instruction_pointer, next_acc = OPERATIONS[opcode](int(value), instruction_pointer, accumulator)

        if instruction_pointer in visited:
            return None

        visited.add(instruction_pointer)
        accumulator = next_acc
    
    return accumulator

with open('input.txt', 'r') as file:
    instructions = list(map(as_instruction, file.read().rstrip("\n").split("\n")))

OPERATIONS = {
    "nop": lambda _, ip, acc: (ip + 1, acc),
    "acc": lambda v, ip, acc: (ip + 1, acc + v),
    "jmp": lambda v, ip, acc: (ip + v, acc) 
}

for i in range(len(instructions)):
    opcode, value = instructions[i]
    if (opcode not in ["nop", "jmp"]):
        continue

    new_opcode = "jmp" if opcode == "nop" else "nop"
    instructions[i] = (new_opcode, value)
    
    result = run(instructions)
    if (result != None):
        print(result)
        break

    instructions[i] = (opcode, value)
