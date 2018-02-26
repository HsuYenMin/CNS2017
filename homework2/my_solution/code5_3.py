import codecs
def read(filename):
    with open(filename, 'r') as f:
        lines = [line for line in f]
    N = int(lines[0][:-1].split()[2], 16)
    E = int(lines[2][:-1].split()[2], 16)
    C = int(lines[4][:-1].split()[2], 16)
    return N, E, C

# ax + by = g = gcd(a, b)
def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

NA, EA, CA = read('./RSA3/Alice')
NB, EB, CB = read('./RSA3/Bob')
if NA == NB:
    print("they use the same module!")

_,S2,_ = xgcd(EB,EA)
S1 = (EB * S2 -1) // EA
_, CA_inv, _ = xgcd(CA, NA)
M = pow(CA_inv, S1, NA) * pow(CB, S2, NB) % NA
messenge = hex(M)[2:]
print(codecs.decode(messenge,encoding="hex"))
