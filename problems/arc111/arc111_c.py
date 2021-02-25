import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
P = list(map(int, input().split()))
motinusi = [None]*N
motimono = [None]*N
for i, p in enumerate(P):
    p -= 1
    motinusi[p] = i
    motimono[i] = p

for i in range(N):
    if A[i] <= B[motimono[i]] and motimono[i] != i:
        print(-1)
        sys.exit()

ans = []
for i, a in sorted(enumerate(A), key=lambda x: x[1]):
    mono = motimono[i]
    if i == mono:
        continue
    nusi = motinusi[i]
    ans.append((i+1, nusi+1))
    motimono[i] = i
    motinusi[i] = i
    motimono[nusi] = mono
    motinusi[mono] = nusi
print(len(ans))
for i, j in ans:
    print(i, j)
