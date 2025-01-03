import time

with open("test.txt") as f:
    lines = f.read().splitlines()

REGISTERS = [int(x.split(": ")[1]) for x in lines[:3]]
program = [int(x) for x in lines[4].split(": ")[1].split(",")]


def get_combo(op):
    if op <= 3:
        return op
    elif op == 4:
        return REGISTERS[0]  # A
    elif op == 5:
        return REGISTERS[1]  # B
    elif op == 6:
        return REGISTERS[2]  # C


def adv(op):  # opcode 0 - combo
    REGISTERS[0] = int(REGISTERS[0] / (2 ** get_combo(op)))


def bxl(op):  # opcode 1 - literal
    REGISTERS[1] = REGISTERS[1] ^ op


def bst(op):  # opcode 2 - combo
    REGISTERS[1] = get_combo(op) % 8


def jnz(op):  # opcode 3 - literal
    if REGISTERS[0] == 0:
        return -1
    else:
        return op


def bxc():  # opcode 4
    REGISTERS[1] = REGISTERS[1] ^ REGISTERS[2]


def out(op, arr):  # opcode 5 - combo
    arr.append(get_combo(op) % 8)


def bdv(op):  # opcode 6 - combo
    REGISTERS[1] = int(REGISTERS[0] / (2 ** get_combo(op)))


def cdv(op):  # opcode 7 - combo
    REGISTERS[2] = int(REGISTERS[0] / (2 ** get_combo(op)))


def execute(program):
    ptr = 0
    to_print = []

    while ptr < len(program):
        opcode = program[ptr]
        operand = program[ptr+1]

        if opcode == 0:
            adv(operand)
        elif opcode == 1:
            bxl(operand)
        elif opcode == 2:
            bst(operand)
        elif opcode == 3:
            jump = jnz(operand)
            if jump != -1:
                ptr = jump - 2
        elif opcode == 4:
            bxc()
        elif opcode == 5:
            out(operand, to_print)
        elif opcode == 6:
            bdv(operand)
        else:
            cdv(operand)

        ptr += 2

    return to_print


start_time = time.time()
output = execute(program)
print(time.time() - start_time, "seconds")
print(','.join([str(x) for x in output]))
print()

# part 2
start_time = time.time()
search = ''.join(str(x) for x in program)
a = 0
match_len = 1

while True:
    REGISTERS[0] = a
    output = execute(program)
    out_str = ''.join(str(x) for x in output)

    if search[-match_len:] == out_str:
        if search == out_str:
            break

        a <<= 3
        match_len += 1
        continue

    a += 1

print(time.time() - start_time, "seconds")
print(a)
