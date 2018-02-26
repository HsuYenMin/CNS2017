#!/usr/bin/python
import signal
import sys
import os
import time

from urlparse import parse_qs
from base64 import b64encode
from base64 import b64decode
from re import match
from Crypto.Cipher import AES

import secret
FLAG = secret.FLAG
KEY = secret.KEY
IV = secret.IV

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[-1])]

def AES_encrypt(m):
    m = pad(m)
    aes = AES.new(KEY, AES.MODE_ECB, IV)
    return b64encode(aes.encrypt(m))

def AES_decrypt(c):
    c = b64decode(c)
    aes = AES.new(KEY, AES.MODE_ECB, IV)
    return unpad(aes.decrypt(c))

def alarm(time):
    def handler(signum, frame):
        print 'Timeout'
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)



def register():
    name = raw_input('Your user name: ').strip()
    pwd = raw_input('Your password: ').strip()
    if not match('^[\w]+$', name) or not match('^[\w]+$', pwd):
        print '[-] Wrong'
        print '[-] User name and password should be composed by letters (a~z, A~Z), digits (0~9) and underscore (_).'
        return
    pt = 'login=' + name + '&role=user' + '&pwd=' +pwd
    print '[+] Your token: ' + AES_encrypt(pt)

def login():
    token = raw_input('Provide your token: ').strip()
    name = raw_input('Provide your username: ').strip()
    pwd = raw_input('Provide your password: ').strip()
    try:
        pt = AES_decrypt(token)
        data = parse_qs(pt, strict_parsing=True)
        if name != data['login'][0] or pwd != data['pwd'][0]:
            print '[-] Authentication failed'
            return
        print '[+] Welcome, %s' % data['login'][0]
        if 'admin' in data['role']:
            print 'Hi admin:', FLAG
    except:
        print '[-] Error'

def main():
    print '--------------------'
    print '[0] Register'
    print '[1] Login'
    print '--------------------'
    num = raw_input().strip()
    if num == '0':
        register()
    elif num == '1':
        login()

if __name__ == '__main__':

    time.sleep(1)

    alarm(30)
    sys.dont_write_bytecode = True
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)

    main()
