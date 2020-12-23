#!/cygdrive/c/Python37/python

import sys, os, re

if len(sys.argv) != 2:
    print("usage: ihex_checksum_verify.py <infile.hex>")
    print("no file given")
    sys.exit(1)

if not sys.argv[1].endswith(".hex"):
    print("usage: ihex_checksum_verify.py <infile.hex>")
    print("file extension not hex")
    sys.exit(2)

if not os.path.exists(sys.argv[1]):
    print("usage: ihex_checksum_verify.py <infile.hex>")
    print("file does not exist")
    sys.exit(3)

if not os.path.isfile(sys.argv[1]):
    print("usage: ihex_checksum_verify.py <infile.hex>")
    print("not a file")
    sys.exit(4)

if not os.access(sys.argv[1], os.R_OK):
    print("usage: ihex_checksum_verify.py <infile.hex>")
    print("file is not readable")
    sys.exit(5)

try:
    open(sys.argv[1])
except:
    print("usage: ihex_checksum_verify.py <infile.hex>")
    print("file is not readable")
    sys.exit(6)

p = re.compile(r'^:(?P<num>..)(?P<address>....)(?P<type>..)(?P<data>.*?)(?P<checksum>..)$')

passed = True
for idx, line in enumerate(open(sys.argv[1]).readlines()):
    m = p.match(line)
    d = m.group("num") + m.group("type") + m.group("address") + m.group("data")
    # d = m.group("num") + m.group("address") + m.group("data")
    s = [int(d[i*2:i*2+2],16) for i in range(len(d)//2)]
    c = ((sum(s) ^ 0xFF) + 1) & 0xFF
    if c != int(m.group("checksum"), 16):
        print(f"checksum error on line {idx+1} => {line}")
        passed = False

if passed:
    print(f"passed")
else:
    print(f"failed")

