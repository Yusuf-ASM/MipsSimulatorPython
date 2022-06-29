from registers import *
# returend = -1


def Xor(rd, rt, rs):
    rs = getReg(rs)
    rt = getReg(rt)
    res = rt ^ rs
    setReg(rd, res)
    return -1



def Or(rd, rt, rs):
    rs = getReg(rs)
    rt = getReg(rt)
    res = rt or rs
    setReg(rd, res)
    return -1



def And(rd, rt, rs):
    rs = getReg(rs)
    rt = getReg(rt)
    res = rt and rs
    setReg(rd, res)
    return -1



def Sub(rd, rt, rs):
    rs = getReg(rs)
    rt = getReg(rt)
    res = rs - rt
    setReg(rd, res)
    return -1



def Add(rd, rt, rs):
    rs = getReg(rs)
    rt = getReg(rt)
    res = rt + rs
    setReg(rd, res)
    return -1



def Slt(rd, rt, rs):
    rs = getReg(rs)
    rt = getReg(rt)
    if rs < rt:
        res = 1
    else:
        res = 0
    setReg(rd, res)
    return -1

