import codecs
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

with open("RSA1/flag.enc", 'rb') as f:
    flag = f.read()

flag = codecs.encode(flag,'hex')
Flag = int(flag,16)
n = 1383529017335793895615038730528059665610606390667095669957559486327
# n_str = " 0d:23:2c:38:a2:2a:fb:7e:e8:dd:b6:d9:25:5e:59:ce:b7:17:e2:cf:58:d5:43:4a:43:4e:87:77"
# if n == int(n_str.replace(":",""),16):
#     print("check n pass!")
# else:
#     print("check n fail!")
p = 1122830395489501760925799210383299
q = 1232179875868643257203600345344573
e = 65537
phi = (p-1)*(q-1)
d = modinv(e,phi)
# if (e * d) % phi == 1:
#     print("check key pass!")
flag_plain = pow(Flag,d,n)
flag_plain = "0" + hex(flag_plain)[2:]
print(codecs.decode(flag_plain,encoding="hex"))
