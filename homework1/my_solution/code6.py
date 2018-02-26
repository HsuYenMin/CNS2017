def hex2IntArr(s):
    # s: a hexidecimal string, e.g. "ff16428b"
    # return value: an integer list, e.g. [255, 22, 66, 139]
    return [int(s[i:i+2], 16) for i in range(0, len(s), 2)]

def xor(intArr0, intArr1):
    return [a^b for a, b in zip(intArr0, intArr1)]

def seeXorResults(index, ciphers):
    c = ciphers[0: index] + ciphers[index + 1:]
    return [xor(ciphers[index], cipher) for cipher in c]

def statistics(xorResults):
    s = []
    for i in range(max([len(t) for t in xorResults])):
        null,cc, np, u, l =0, 0, 0, 0, 0
        for row in xorResults:
            if i < len(row):
                if     row[i] == 0:
                    null += 1
                elif   row[i] < 32:
                    cc += 1
                elif row[i] < 64:
                    np += 1
                elif row[i] < 96:
                    u  += 1
                else:
                    l  += 1
        s.append([null, cc, np, u, l])
    return s

def sync(ciphers, answers):
    for i in range(max([len(c) for c in ciphers])):
        haveAns, notSolve, ansIdx = False, False, None
        for j, answer in enumerate(answers):
            if i < len(answer):
                if answer[i] != None:
                    haveAns = True
                    ansIdx  = j 
                else:
                    notSolve = True
        if haveAns and notSolve and ansIdx != None:
            key = ord(answers[ansIdx][i]) ^ ciphers[ansIdx][i]
            for j, answer in enumerate(answers) :
                if i < len(answer):
                    answers[j][i] = chr( key ^ ciphers[j][i])

def display(answers):
    for answer in answers:
        for a in answer:
            if a == None:
                print('*', end='')
            else:
                print(a, end='')
        print()

if __name__ == "__main__":
    with open("MTP/cipher", 'r') as f:
        strings = [line.strip('\n') for line in f]
    ciphers = [hex2IntArr(string) for string in strings]
    answers = [[None]*len(cipher) for cipher in ciphers]
    display(answers)
    for i, cipher in enumerate(ciphers):
        xorResults = seeXorResults(i, ciphers)
        distributions = statistics(xorResults)
        for j, distribution in enumerate(distributions):
            if distribution[1] == 0 and distribution[2] == 0:
                answers[i][j] = ' '
    sync(ciphers,answers)
    display(answers)

