#!/usr/bin/env python
import hashlib
import os
import random
import signal
import sys
import time

def alarm(time):
    def handler(signum, frame):
        print 'You need to be faster'
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)

def sha1(content):
    Hash=hashlib.sha1()
    Hash.update(content)
    return Hash.digest()

def POW():
    randomstring=hex(random.randint(0,16777216))[2:]
    alarm(120)
    print "Finish this challenge in two minute"
    print "And your input size should be smaller than 400byte"
    Input=raw_input("Give me the X such that sha1(X)=??????????????????????????????????{:0>6}:".format(randomstring)).decode("hex")
    UserX=Input
    if len(UserX)>400:
        print "Input size too big!!"
        exit()
    UserHash=sha1(UserX).encode("hex")
    if sha1(UserX).encode("hex")[-6:]!="{:0>6}".format(randomstring):
        print "Wrong"
        exit()
    print "Great!!"
    return UserHash,UserX

def collision(UserHash,UserX):
    Input=raw_input("Now Give me the Y such that sha1(X)==sha1(Y):").decode("hex")
    if Input==UserX:
        print "Y can't be the same as X"
        exit()
    UserHash2=sha1(Input).encode("hex")
    if UserHash2!=UserHash :
        print "Wrong"
        exit()

def flag():
    flag=open("flag.txt").read()
    print flag


if __name__ == '__main__':
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)
    UserHash,UserX=POW()
    collision(UserHash,UserX)
    flag()
    exit()
