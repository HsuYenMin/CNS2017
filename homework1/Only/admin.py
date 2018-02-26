#!/usr/bin/env python
import signal
import sys
import os
import time
import base64
import random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

sys.dont_write_bytecode = True
import secret

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[-1])]


def alarm(time):
    def handler(signum, frame):
        print 'Timeout'
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)

def sha256(content):
    Sha256 = SHA256.new()
    Sha256.update(content)
    return Sha256.digest()

def checkIntegrity(message, digest):
    sha256 = SHA256.new()
    sha256.update(message)
    if base64.b64encode(sha256.digest()) != digest:
        print 'Integrity error!'
        exit()


def findPW(ID):
    password = ''
    for each in secret.userAndPw:
        if each.split(':')[0] == ID:
            password = each.split(':')[1]
    if password == '':
        print 'ID not found!'
        exit()
    return password


def first():
    try:
        recv = raw_input('You should send your ID and a random string to me: ')
        ID, N, digest = recv.split('||')
    except:
        print 'Format error!'
        exit()
    checkIntegrity(ID + '||' + N, digest)
    return ID, N


def second(ID, Nc, password, Ns):
    # authenticate the server
    cipher = sha256(password + '||' + ID + '||' + Nc + '||' + "login")
    print Ns + '||' + base64.b64encode(cipher)


def third(ID, password, Ns):
    try:
        recv = raw_input('You send me your ID, my random string and your action in base64encode'+
            'and the Mac\n'+
            'Like this Base64encode(ID+"||"+Ns+"||"+action)+"||"+Base64encode(sha256(password+"||"+ID+"||"+Ns+"||"+action))')
        Message,Mac = recv.split('||')
    except:
        print 'Format error!'
        exit()
    Message=base64.b64decode(Message)
    print Message
    checkIntegrity(password + "||" + Message, Mac)
    plaintext=Message.split("||")
    if plaintext[0] == ID and plaintext[1] == Ns:
        print 'Welcome! ' + ID
        if ID == 'admin' and plaintext[-1] == "printflag":
            print 'The flag is: ' + secret.FLAG

    else:
        print "Something is wrong"
        exit()


if __name__ == '__main__':
    alarm(60)
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)

    print 'Let me sleep first . . .'
    time.sleep(5)
    print 'I\'m back!'

    ID, Nc = first()
    password = findPW(ID)
    Ns = str(random.randint(100, 99999))
    second(ID, Nc, password, Ns)
    third(ID, password, Ns)

