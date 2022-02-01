import sys
import itertools

S1 = input()
S2 = input()
S3 = input()
d = set(S1+S2+S3)
ngs = set(S1[0]+S2[0]+S3[0])
if len(d) > 10:
    print('UNSOLVABLE')
    sys.exit(0)

def mkN(S, word2num):
    ret = 0
    for s in S:
        ret *= 10
        ret += word2num[s]
    return ret

def isok(word2num):
    return mkN(S1, word2num)+mkN(S2, word2num) == mkN(S3, word2num)

d = list(d)
for nums in itertools.permutations(range(10)):
    word2num = {}
    flg = False
    for w, n in zip(d, nums):
        if n==0:
            flg = w in ngs
        word2num[w] = n
    if flg:
        continue
    if isok(word2num):
        for S in [S1, S2, S3]:
            print(mkN(S, word2num))
        sys.exit(0)
print('UNSOLVABLE')
