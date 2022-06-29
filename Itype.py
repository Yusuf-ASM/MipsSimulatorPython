from Rtype import *


def Beq(rs, rt, next):
    rs = getReg(rs)
    rt = getReg(rt)
    if rs == rt:
        return next
    return -1


def Bne(rs, rt, next):
    rs = getReg(rs)
    rt = getReg(rt)
    if rs != rt:
        return next
    return -1


def Blez(rs, next):
    rs = getReg(rs)
    if rs <= 0:
        return next
    return -1


def Bgtz(rs, next):
    rs = getReg(rs)
    if rs > 0:
        return next
    return -1


def Addi(rt, rs, imm):
    rs = getReg(rs)
    res = imm + rs
    setReg(rt, res)
    return -1


def Slti(rt, rs, imm):
    rs = getReg(rs)
    if rs < imm:
        res = 1
    else:
        res = 0
    setReg(rt, res)
    return -1



def Andi(rt, rs, imm):
    rs = getReg(rs)
    res = imm and rs
    setReg(rt, res)
    return -1



def Ori(rt, rs, imm):
    rs = getReg(rs)
    res = imm or rs
    setReg(rt, res)
    return -1



def Xori(rt, rs, imm):
    rs = getReg(rs)
    res = imm ^ rs
    setReg(rt, res)
    return -1

