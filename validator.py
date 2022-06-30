from registers import registers, supported

fileName = "a.asm"
source = open(fileName, 'r')
instruction = list(map(lambda x: x.strip(), source.readlines()))
jumps = []

# find jumps
for ins in instruction:
    if ':' in ins:
        jumps.append(ins[:-1])
        continue

line = 0
for ins in instruction:
    ins = ins.lower()
    if ins == "" or ":" in ins:
        continue

    temp = ins.find(" ")
    if temp == -1:
        print("invalid instruction at line ", line)
        continue
    elif ins[:temp] not in supported:
        print("unsupported instruction at line ", line)
        continue

    opcode = ins[:temp]
    var = ins[temp + 1:].split(',')

    if supported[opcode] == 4 and 3 != len(var):
        print("wrong input number at line ", line)
    elif supported[opcode] != 4 and supported[opcode] != len(var):
        print("wrong input number at line ", line)
    if supported[opcode] == 2 and var[0] not in registers:
        print("wrong registers number at line ", line)
    elif supported[opcode] == 4 and (var[0] not in registers or var[1] not in registers):
        print("wrong registers number at line ", line)
    elif supported[opcode] == 3 and (var[0] not in registers or var[1] not in registers or var[2] not in registers):
        print("wrong registers number at line ", line)
    line += 1
