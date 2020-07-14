import sys, collections
N = int(input())
S = [str(input()) for _ in range(N)]
d = collections.Counter(S)
for k in 'AC WA TLE RE'.split():
    print(f'{k} x {d[k]}')
