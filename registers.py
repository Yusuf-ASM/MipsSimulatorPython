def getReg(reg):
    return registersList[registers[reg]]


def setReg(reg, data):
    registersList[registers[reg]] = data


registers = {
    '$zero': 0,
    '$0': 0,
    '$at': 1,
    '$v0': 2,
    '$v1': 3,
    '$a0': 4,
    '$a1': 5,
    '$a2': 6,
    '$a3': 7,
    '$t0': 8,
    '$t1': 9,
    '$t2': 10,
    '$t3': 11,
    '$t4': 12,
    '$t5': 13,
    '$t6': 14,
    '$t7': 15,
    '$s0': 16,
    '$s1': 17,
    '$s2': 18,
    '$s3': 19,
    '$s4': 20,
    '$s5': 21,
    '$s6': 22,
    '$s7': 23,
    '$t8': 24,
    '$t9': 25,
    '$k0': 26,
    '$k1': 27,
    '$gp': 28,
    '$sp': 29,
    '$fp': 30,
    '$ra': 31,
}

supported = {
    "j" : 1,
    "blez": 2,
    "bgtz": 2,
    "xor": 3,
    "or": 3,
    "and": 3,
    "sub": 3,
    "add": 3,
    "slt": 3,
    "addi": 4,
    "slti": 4,
    "andi": 4,
    "ori": 4,
    "xori": 4,
    "beq": 5,
    "bne": 5,
}

registersList = [0] * 32

jumps = {}

def displayRegisters():
    for key in registers:
        index = registers[key]
        print(f" reg = {key}, value = {registersList[index]}")

