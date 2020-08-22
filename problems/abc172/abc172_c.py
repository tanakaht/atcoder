import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


SA, SB = [0]*(N+1), [0]*(M+1)
for i, a in enumerate(A):
    SA[i + 1] = SA[i] + a

for i, b in enumerate(B):
    SB[i + 1] = SB[i] + b

piv = M
ans = 0
flg = False
for i, a in enumerate(SA):
    while SB[piv] + SA[i] > K:
        piv -= 1
        if piv < 0:
            flg = True
            break
    if flg:
        break
    ans = max(ans, piv+i)
print(ans)


