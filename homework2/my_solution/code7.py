import codecs
import base64

def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

p = ["00 e0 6f 75 52 05 d1 06 35 02 ac 80 44",
"12 7f 4a ea da 8a c5 ad f8 83 0c 61 f5 ea 0c",
"71 71 4c 8e a1 a8 10 6a 2a 69 49 80 7d 2d 0f",
"7d c0 38 77 f3 52 21 b6 97 26 cd c2 e6 ab 35",
"11 52 db ab 54 7d 52 c1 71 9b 7e 79 76 ab 2d",
"5a e6 62 a2 df e2 e5 71 51 ef 1f ce dc a7 e8",
"e8 94 7c 34 6d 32 b6 6e 76 4c 44 93 cb 71 f5",
"48 a4 dd c0 7b 8d 63 e2 fe 8d 8b fc aa cb e0",
"52 9a 22 fb 8a cd 8f 7b df c9 23"]
p = int("".join(p).replace(" ",""),16)

q = ["00",
"d0 80 09 43 20 be f1 6c 0c d4 55 38 d1 13 6b",
"13 28 a6 8a c9 90 f3 38 d3 07 7d e1 8e 03 67",
"18 b3 9a 17 47 84 96 fb ff d8 93 41 fb 39 83",
"8a 00 35 0c 43 6b f3 1a 7b c0 73 bb 6c c1 de",
"ef f4 b0 37 98 78 b5 43 a3 c6 c1 90 05 24 89",
"72 5b 02 46 f1 11 61 52 cb 14 1b c6 7a 17 bd",
"ef fa e7 10 8d c5 5e a9 2f 2b e0 fa 76 a4 ab",
"a7 2c 9b 8b 12 d6 a0 3e b5 5b 57 37 87 06 c7",
"ee ac a8 62 68 dc a4 7b"]
q = int("".join(q).replace(" ",""),16)

dp = ["00 ca ac fc",
"a6 90 a8 1d 51 db d3 49 95 af 9a 92 5e 19 f3",
"3d e7 08 47 d7 f3 d2 ee 84 44 21 cb bf f6 4e",
"5e 5c 71 66 59 41 16 49 8d f6 c2 92 7c 08 18",
"c0 67 32 82 91 48 13 a4 c2 ac 9d 45 d0 a7 e0",
"f0 cd ce 39 5c 72 75 ee c9 6b 90 27 bc ec 2f",
"eb 81 75 3b 5b 5f 24 b6 e1 46 bf 68 96 b3 92",
"1b 5b 0f ab 7a 36 79 7f b4 c0 e0 59 7d 0c 56",
"37 c0 f2 9d 82 b0 2e d1 24 07 94 38 49 2e 24",
"ca 11 54 9b 3f"]
dp = int("".join(dp).replace(" ",""),16)

dq = ["0a 03 dc 6e 09 08 a2",
"f8 19 b5 a9 52 4d 58 ad 70 02 27 dd ca c8 d7",
"a6 07 1c f9 02 f8 9b 59 3c 6a 84 20 52 23 20",
"4d 82 80 98 b2 36 ab 10 92 74 68 17 ea b5 28",
"bc 40 ed 81 a1 a3 1b bc e5 b1 cf 35 1c 71 cf",
"e3 2b de c4 35 72 c9 ca 80 5f b6 c0 49 9c 18",
"1c ad fc 8d 48 ff 5c 5c 97 46 6a 0a f5 84 61",
"83 a6 ec 68 a6 1f 44 d1 a9 fa 0e 8e a3 9d 03",
"9d 7f 80 9f b3 df 1c 88 46 02 ad 23 ec fd 8c",
"39"]
dq = int("".join(dq).replace(" ",""),16)

qinv = ["00 98 62 c0 2f 29 dd 2c 9a 5a 03",
"e1 17 f9 c8 3f 1d 6e eb 47 5b 88 ae fe 5d 42",
"a3 01 b5 27 3c 78 ba 58 38 30 fa d2 2d b6 0e",
"f7 16 47 42 88 7b aa e9 15 ad 97 a8 78 f6 ce",
"a9 fb 58 bc 8c 39 e4 e9 c1 84 dd d3 0a 0b e2",
"72 81 d7 2e 09 fc 0e 14 1f e7 2f 08 38 e1 21",
"57 94 26 fc 4a 3b e7 6e 23 bf bf 8d f6 4c 91",
"ed 53 aa 32 0a 7a b0 3e 7d 80 c3 73 ed 1c f3",
"87 e0 40 c1 47 4f 42 e6 0d b2 4c f2 30"]
qinv = int("".join(qinv).replace(" ",""),16)

factor_p_1 = [2, 23071, 101611, 279143, 15105469783,
7972027789830578494097472474489956607943252900350057430472351710237513519724020890748339214078090043585732875195937707006695010042852988627031410268281669443729208551498638413658730485207715968285179856542275521427342837670239580562069075710537473671805106550061794383737518698386989]
factor_q_1 = [2,
73206889196716734112412134681537560774938373207751893124999720610343234871637837334075317207649153233907098487174448497100134854614834655345079432951814523216607070154241232136161486589658757926215170203408278028798239721151142979819444956402758956905611734069659395670679999669491208735748943832493237097021]


m1 = 2
a1 = 1

m2 = 1
for i in range(1,len(factor_p_1)):
    m2 = m2 * factor_p_1[i]
a2 = dp % m2

m3 = factor_q_1[1]
a3 = dq % m3

M = m1 * m2 * m3
M1 = m2 * m3
M2 = m1 * m3
M3 = m1 * m2

_, t1, _ = xgcd(M1, m1)
_, t2, _ = xgcd(M2, m2)
_, t3, _ = xgcd(M3, m3)

d = a1 * t1 * M1 + a2 * t2 * M2 + a3 * t3 * M3
d = d % M

_, e, _= xgcd(d,M)

with open("./Need_your_help/flag.enc", 'rb') as f:
    flag = f.read()
flag = codecs.encode(flag,'hex')
Flag = int(flag,16)
n = p * q
flag_plain = pow(Flag,d,n)
flag_plain = "0" + hex(flag_plain)[2:]
print(codecs.decode(flag_plain,encoding="hex"))
