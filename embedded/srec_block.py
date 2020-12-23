#!/cygdrive/c/Python37/python

import sys, os, re

if len(sys.argv) != 2:
    print("usage: srec_checksum_verify.py <infile.srec>")
    print("no file given")
    sys.exit(1)

if not (sys.argv[1].endswith(".s37") or sys.argv[1].endswith(".S37")):
    print("usage: srec_checksum_verify.py <infile.srec>")
    print("file extension not s37")
    sys.exit(2)

if not os.path.exists(sys.argv[1]):
    print("usage: srec_checksum_verify.py <infile.srec>")
    print("file does not exist")
    sys.exit(3)

if not os.path.isfile(sys.argv[1]):
    print("usage: srec_checksum_verify.py <infile.srec>")
    print("not a file")
    sys.exit(4)

if not os.access(sys.argv[1], os.R_OK):
    print("usage: srec_checksum_verify.py <infile.srec>")
    print("file is not readable")
    sys.exit(5)

try:
    open(sys.argv[1])
except:
    print("usage: srec_checksum_verify.py <infile.srec>")
    print("file is not readable")
    sys.exit(6)

# S19 style uses 16 bit address
# p = re.compile(r'^S(?P<type>.)(?P<num>..)(?P<address>....)(?P<data>.*?)(?P<checksum>..)$')

# S37 style uses 32 bit address
p = re.compile(r'^S(?P<type>.)(?P<num>..)(?P<address>........)(?P<data>.*?)(?P<checksum>..)$')

def checksum():
    passed = True
    for idx, line in enumerate(open(sys.argv[1]).readlines()):
        m = p.match(line)
        if not m:
            print("no match at line %s => %s" % (idx+1, line), end = "")
            continue
        d = m.group("num") + m.group("address") + m.group("data")
        s = [int(d[i*2:i*2+2],16) for i in range(len(d)//2)]
        c = ((sum(s) ^ 0xFF)) & 0xFF
        if c != int(m.group("checksum"), 16):
            print(f"checksum error on line {idx+1} => {line}")
            passed = False
    return passed

def blocks():
    b = []
    addr_ = 0
    length_ = 0
    for idx, line in enumerate(open(sys.argv[1]).readlines()):
        if line.strip() == "":
            continue
        m = p.match(line)
        if not m:
            print("no match at line %s => %s" % (idx+1, line), end = "")
            continue
        if m.group("type") != "3":
            continue
        # only data records
        addr = int(m.group("address"), 16)
        length = int(m.group("num"), 16)
        if b == []:
            # on first iteration
            b.append([addr])
        else:
            # later addr_ and length_
            if addr_ + length_ < addr:
                b[-1].append(addr_ + length_)
                b.append([addr])
        addr_ = addr
        length_ = length
    if b != []:
        b[-1].append(addr_ + length_)
    return b

if __name__ == "__main__":
    print("checksum => %s" % {False: "failed", True: "passed"}[checksum()])
    #
    for idx, b in enumerate(blocks()):
        x,y = b
        print(f"block {idx+1}: [0x%08X .. 0x%08X], size = 0x%04X = %s [B] = %.2f [kB]" % (x,y,y-x,y-x,(y-x)/1024))

