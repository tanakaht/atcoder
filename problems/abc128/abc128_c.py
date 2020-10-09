import sys

input = sys.stdin.readline
N, M = map(int, input().split())
S = [0] * M

for i in range(M):
    k, *ss = map(int, input().split())
    for s in ss:
        s -= 1
        S[i] += pow(2, s)

for i, p in enumerate(map(int, input().split())):
    S[i] += p * pow(2, N)

ans = 0
for b in range(pow(2, N)):
    b += pow(2, N)
    flg = True
    for i in range(M):
        flg = flg and (bin(S[i] & b)[1:].count('1') % 2 == 0)
    ans += flg
print(ans)
