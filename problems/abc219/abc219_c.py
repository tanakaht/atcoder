import sys

X = input()
chr2idx = {x: i for i, x in enumerate(X)}
def get_idx(s):
    ret = ''.join([chr(chr2idx[c]) for c in s])
    return ret
N = int(input())
S = sorted([input() for _ in range(N)], key=lambda x: get_idx(x))
print(*S, sep='\n')
