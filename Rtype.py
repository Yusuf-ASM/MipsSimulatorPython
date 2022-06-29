from registers import *


def Xor(rd, rt, rs):
    rs = getReg(rs)
    rt = getReg(rt)
    res = rt ^ rs
    setReg(rd, res)


def Or(rd, rt, rs):
    rs = getReg(rs)
    rt = getReg(rt)
    res = rt or rs
    setReg(rd, res)


def And(rd, rt, rs):
    rs = getReg(rs)
    rt = getReg(rt)
    res = rt and rs
    setReg(rd, res)


def Sub(rd, rt, rs):
    rs = getReg(rs)
    rt = getReg(rt)
    res = rs - rt
    setReg(rd, res)


def Add(rd, rt, rs):
    rs = getReg(rs)
    rt = getReg(rt)
    res = rt + rs
    setReg(rd, res)


def Slt(rd, rt, rs):
    rs = getReg(rs)
    rt = getReg(rt)
    if rs < rt:
        res = 1
    else:
        res = 0
    setReg(rd, res)
