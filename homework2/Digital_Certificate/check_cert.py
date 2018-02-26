#!/usr/bin/python

import signal, sys, os, time
from OpenSSL import crypto
from base64 import b64decode

import secret
FLAG = secret.FLAG

def alarm(time):
    def handler(signum, frame):
        print 'Timeout. Bye~'
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)


def check():

    global FLAG

    b64_cert_text = raw_input(': ').strip()
    cert_text = b64decode(b64_cert_text)
	
    print '\n: hmmm..... let me check.\n'
    time.sleep(2)    

    cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_text)
	
    # The service will do some certificate checking here.
    # If you pass the chekcing process, you will get the flag.
			
    return


if __name__ == '__main__':

    alarm(120)
    sys.dont_write_bytecode = True
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0) 

    check()
