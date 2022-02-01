import sys

N, K = map(int, input().split())
n = int(1e5)
MOD = n
def transition(x):
    ret = x
    for i in range(5):
        ret += (x//(10**i))%10
    return ret % MOD

trans = [i for i in range(n)]
for i in range(K.bit_length()):
    trans = [trans[trans[j]] for j in range(n)]
    if (K>>(K.bit_length()-i-1))&1:
        trans = [transition(trans[j]) for j in range(n)]
print(trans[N])
