def speed(val):
    return float(int('0x'+ val, 0))

def rpm(val):
    upper = float(int('0x'+ val[0:2], 0)) * 256
    lower = float(int('0x'+ val[2:4], 0))
    print "worked: ", val
    return (upper + lower) / 4
