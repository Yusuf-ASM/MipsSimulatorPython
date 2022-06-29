from Itype import *

# Variables
fileName = "a.asm"
source = open(fileName, 'r')
current = 0
instruction = list(map(lambda x: x.strip(), source.readlines()))

# Index of jumps
for i in range(len(instruction)):
    tmp = instruction[i]
    if ':' in tmp:
        jumps[tmp[:-1]] = i


# Execute function
def Execute(ins):
    if ins == "":
        return -1

    elif ':' in ins:
        return -1

    tmp = ins.find(" ")
    fun = ins[:tmp]
    var = ins[tmp + 1:].split(',')
    opcode = supported[fun]

    if opcode == 1:
        return jumps[var[0]]

    elif opcode == 2:
        p0 = var[0]
        p1 = var[1]
        r = {}
        exec(f"r = {fun[0].upper() + fun[1:]}('{p0}','{p1}')",globals(),r)
        print(r['r'])
        return r['r']

    elif opcode == 3:
        p0 = var[0]
        p1 = var[1]
        p2 = var[2]
        exec(f"{fun[0].upper() + fun[1:]}('{p0}','{p1}','{p2}')")

    elif opcode == 4:
        p0 = var[0]
        p1 = var[1]
        p2 = var[2]
        exec(f"{fun[0].upper() + fun[1:]}('{p0}','{p1}',{p2})")

    elif opcode == 5:
        p0 = var[0]
        p1 = var[1]
        p2 = var[2]
        r = {}
        exec(f"r = {fun[0].upper() + fun[1:]}('{p0}','{p1}','{p2}')")
        return r['r']

    return -1


# Main loop
while current != len(instruction):
    temp = Execute(instruction[current])
    if temp == -1:
        current += 1
    else:
        current = temp

displayRegisters()
source.close()
