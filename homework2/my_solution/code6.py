from pwn import remote
import base64
import sys

with open(sys.argv[1], "rb") as f:
    lines = [line for line in f]
cert = b''
for line in lines:
    cert += line

certTosent = base64.b64encode(cert)
r = remote("140.112.31.109",10005)
ss = r.recvuntil(': ')
print(ss.decode)
r.sendline(certTosent)
ss = r.recvuntil('VALUABLE_INFORMATION{Our_boss_is_Tom!}')
print(ss.decode())
r.close()
