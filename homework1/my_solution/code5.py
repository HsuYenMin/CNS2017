import hashlib
import random
from pwn import remote
import codecs

with open('shattered-1.pdf', 'rb') as f:
    A = f.read()[:320]
with open('shattered-2.pdf', 'rb') as f:
    B = f.read()[:320]

print(A==B)
print(hashlib.sha1(A).hexdigest() == hashlib.sha1(B).hexdigest())

r = remote("140.112.31.109",10001)
xs = r.recv(timeout = 0.1).decode("utf-8").split("\n")
for line in xs:
    print(line)
target = xs[2][-7:-1]
random.seed()
print(target)

while True:
    i = random.getrandbits(64)
    ib = hex(i)[2:].encode('utf-8')
    h = hashlib.sha1(A+ib).hexdigest()
    if h[-6:] == target:
        break

temp = codecs.encode(A+ib, encoding='hex')
print(temp)
r.sendline(temp)
xs = r.recv(timeout = 0.1).decode("utf-8").split("\n")
for line in xs:
    print(line)
temp = codecs.encode(B+ib, encoding='hex')
print(temp)
r.sendline(temp)
xs = r.recv(timeout = 0.1).decode("utf-8").split("\n")
for line in xs:
    print(line)
