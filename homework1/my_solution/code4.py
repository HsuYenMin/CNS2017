from pwn import remote
import enchant
import copy
import base64
def shift(i,cs):
    plaintext = copy.copy(cs)
    for idx,c in enumerate(cs):
        v = ord(c)
        p = i + ord(c)
        if v >= 97 and v <= 122 and p > 122 or v >= 65 and v <= 90 and  p > 90:
            plaintext[idx] = chr(p-26)
        elif v >= 97 and v <= 122 or v >=65 and v <= 90:
            plaintext[idx] = chr(p)
    return plaintext

r = remote("140.112.31.109",10000)
# round 1
xs = r.recv(timeout = 0.1).decode("utf-8").split("\n")
xs += r.recv(timeout = 0.1).decode("utf-8").split("\n")
# I don't know why it can't read in one time. A single line works in ipython.
ss = []
for line in xs:
    print(line)
    if line[:2] == "m1" or line[:2] == "c1" or line[:2] == "c2":
        ss = ss + [line]
ss = [line[5:] for line in ss]
codebook = {}
nShift = ord(ss[0][0]) - ord(ss[1][0])
if nShift < 0:
    nShift += 26
plaintext = list(ss[2])
plaintext = shift(nShift,plaintext)
print("".join(plaintext))
answer = "".join(plaintext) + '\n' 
r.send(answer.encode("utf-8"))
# ruond 2
xs = r.recv(timeout = 0.1).decode("utf-8").split("\n")
xs += r.recv(timeout = 0.1).decode("utf-8").split("\n")
for line in xs:
    print(line)
    if line[:2] == "c1":
        ss = line
cs = list(ss[5:])
possibleAns=["".join(shift(i, cs)) for i in range(26)]
d = enchant.Dict("en_US") 
argmax = max(enumerate(possibleAns), key= lambda x: sum([d.check(word) for word in x[1].strip().split()]))
answer = possibleAns[argmax[0]]
print(answer)
r.sendline(answer.encode("utf-8"))
# round 3 
xs = r.recv(timeout = 0.1).decode("utf-8").split("\n")
xs += r.recv(timeout = 0.1).decode("utf-8").split("\n")
ss = []
for line in xs:
    print(line)
    if line[:2] == "m1" or line[:2] == "c1" or line[:2] == "c2":
        ss = ss + [line[5:]]
initShift = ord(ss[0][0]) - ord(ss[1][0])
answer = list(ss[2])
for (idx,c) in enumerate(answer):
        v = ord(c)
        t = initShift - idx
        while t < 0:
            t += 26
        p = ord(c) + t
        if v >= 97 and v <= 122 and p > 122 or v >= 65 and v <= 90 and  p > 90:
            answer[idx] = chr(p-26)
        elif v >= 97 and v <= 122 or v >=65 and v <= 90:
            answer[idx] = chr(p)
answer = "".join(answer)
print(answer)
r.sendline(answer.encode("utf-8"))
# round 4
xs = r.recv(timeout = 0.1).decode("utf-8").split("\n")
xs += r.recv(timeout = 0.1).decode("utf-8").split("\n")
ss = []
for line in xs:
    print(line)
    if line[:2] == "m1" or line[:2] == "c1" or line[:2] == "c2":
        ss = ss + [line[5:]]
r.sendline("give me the hint".encode("utf-8"))
# round 5
xs = r.recv(timeout = 0.1).decode("utf-8").split("\n")
xs += r.recv(timeout = 0.1).decode("utf-8").split("\n")
ss = []
for line in xs:
    print(line)
    if line[:2] == "m1" or line[:2] == "c1" or line[:2] == "c2":
        ss = ss + [line[5:]]
codebook = [-1]*len(ss[1])
for i, c in enumerate(ss[1]):
    idx = -1
    for j, m in enumerate(ss[0]):
        if c == m:
            idx = j
    codebook[i] = idx
answer = [' '] * len(ss[1])
for i, c in enumerate(ss[2]):
    answer[codebook[i]] = c
answer = "".join(answer).strip()
print(answer)
r.sendline(answer.encode("utf-8"))
# round 6
xs = r.recv(timeout = 0.1).decode("utf-8").split("\n")
xs += r.recv(timeout = 0.1).decode("utf-8").split("\n")
ss = []
for line in xs:
    print(line)
    if line[:2] == "m1" or line[:2] == "c1" or line[:2] == "c2":
        ss = ss + [line[5:]]
w = -1
for i in range(4,11):
    s = ""
    for j in range(0, len(ss[1]), i):
        s += ss[0][j]
    if s == ss[1][:len(s)]:
        w = i
        break

print("the width is: ", w)
answer = [" "]*len(ss[2])
k = 0
for i in range(w):
    for j in range(i, len(ss[2]), w):
        answer[j] = ss[2][k]
        k += 1


answer = "".join(answer).strip()
print(answer)
r.sendline(answer.encode("utf-8"))
# round 7
xs = r.recv(timeout = 0.1).decode("utf-8").split("\n")
xs += r.recv(timeout = 0.1).decode("utf-8").split("\n")
for line in xs:
    print(line)
    if line[:2] == "c1":
        ss = line[5:]
ss = base64.b64decode(ss.encode("utf-8"))
print(ss)
r.sendline(ss)

xs = r.recv(timeout = 0.1).decode("utf-8").split("\n")
for line in xs:
    print(line)
