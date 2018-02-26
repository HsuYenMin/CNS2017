from pwn import remote
import base64

# step 1
r = remote("140.112.31.109",10004)
ss = r.recvuntil("[1] Login\n--------------------\n").decode()
print(ss[:-1])
r.sendline('0'.encode())
print(0)
s  = r.recvuntil("Your user name: ").decode()
x = 'a'*20
r.sendline(x.encode())
print(s + x)
s  = r.recvuntil("Your password: ").decode()
y = "123"
r.sendline(y.encode())
print(s + y)
s = r.recvuntil("[+] Your token: ").decode()
print(s, end="")
s = r.recvline()[:-1]
print(s)
step1result = base64.b64decode(s.decode())
red = step1result[:16]
orange = step1result[16:32]
r.close()

# step 2
r = remote("140.112.31.109",10004)
ss = r.recvuntil("[1] Login\n--------------------\n").decode()
print(ss[:-1])
r.sendline('0'.encode())
print(0)
s  = r.recvuntil("Your user name: ").decode()
x = 'a'*11
r.sendline(x.encode())
print(s + x)
s  = r.recvuntil("Your password: ").decode()
y = "admin"
r.sendline(y.encode())
print(s + y)
s = r.recvuntil("[+] Your token: ").decode()
print(s, end="")
s = r.recvline()[:-1]
print(s)
step2result = base64.b64decode(s.decode())
green = step2result[32:]
r.close()

# step 3
r = remote("140.112.31.109",10004)
ss = r.recvuntil("[1] Login\n--------------------\n").decode()
print(ss[:-1])
r.sendline('0'.encode())
print(0)
s  = r.recvuntil("Your user name: ").decode()
x = 'a' * 16
r.sendline(x.encode())
print(s + x)
s  = r.recvuntil("Your password: ").decode()
y = 'b' * 11
r.sendline(y.encode())
print(s + y)
s = r.recvuntil("[+] Your token: ").decode()
print(s, end="")
s = r.recvline()[:-1]
print(s)
step3result = base64.b64decode(s.decode())
blue = step3result[32:48]
r.close()
token = red + blue + orange + green
Token = base64.b64encode(token).decode()

# step 4
r = remote("140.112.31.109",10004)
ss = r.recvuntil("[1] Login\n--------------------\n").decode()
print(ss[:-1])
r.sendline('1'.encode())
print(1)
s  = r.recvuntil("Provide your token: ").decode()
r.sendline(Token.encode())
print(s + Token)
s  = r.recvuntil("Provide your username: ").decode()
username = 'a' * 10
r.sendline(username.encode())
print(s + username)
s = r.recvuntil("Provide your password: ").decode()
pwd = 'b'*11 + 'a'*10
r.sendline(pwd.encode())
print(s + pwd)
ss = r.recvuntil("Hi admin:").decode()
print(ss[:-1], end=" ")
s = r.recvline()[:-1]
print(s)
r.close()
