def as_instruction(line):
    opcode, value = line.split(" ")
    return (opcode, int(value))

with open('input.txt', 'r') as file:
    instructions = list(map(as_instruction, file.read().rstrip("\n").split("\n")))

OPERATIONS = {
    "nop": lambda _, ip, acc: (ip + 1, acc),
    "acc": lambda v, ip, acc: (ip + 1, acc + v),
    "jmp": lambda v, ip, acc: (ip + v, acc) 
}

instruction_pointer = 0
accumulator = 0

visited = set([])

while True:
    opcode, value = instructions[instruction_pointer]
    instruction_pointer, next_acc = OPERATIONS[opcode](int(value), instruction_pointer, accumulator)

    if instruction_pointer in visited:
        print(accumulator)
        break

    visited.add(instruction_pointer)
    accumulator = next_acc