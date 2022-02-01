import sys

N, K, P = map(int, input().split())
A = list(map(int, input().split()))
Afh, Ash = A[:N//2], A[N//2:]
Xfh = [[] for _ in range(N//2+1)]
Xsh = [[] for _ in range(N-N//2+1)]
Xfh[0].append(0)
Xsh[0].append(0)
for a in Afh:
    for k in range(len(Xfh)-2, -1, -1):
        for x in Xfh[k]:
            Xfh[k+1].append(x+a)
for k in range(len(Xfh)):
    Xfh[k] = sorted(Xfh[k])
for a in Ash:
    for k in range(len(Xsh)-2, -1, -1):
        for x in Xsh[k]:
            Xsh[k+1].append(x+a)
for k in range(len(Xsh)):
    Xsh[k] = sorted(Xsh[k])[::-1]

ans = 0
for k in range(len(Xfh)):
    if K-k >= len(Xsh):
        continue
    idx = 0 # ちょうど超えたとこ
    for xfh in Xfh[k]:
        while idx<len(Xsh[K-k]) and Xsh[K-k][idx]+xfh>P:
            idx += 1
        ans += len(Xsh[K-k])-idx
print(ans)
