import sys
L, R = map(int, input().split())
MOD = int(1e9+7)

# [1, x]でやった時
def count(x):
    ret = 0
    c = 1
    v = 1
    while v<=x:
        ret = (ret+(x-v+1)*(x+v)//2)%MOD
        c += 1
        v *= 10
    return ret
print((count(R)-count(L-1))%MOD)
