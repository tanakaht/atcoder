import sys

N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
if S[0] == 1:
    S = [s^1 for s in S]
    T = [t^1 for t in T]
if sum(T)==0:
    print(M)
elif sum(S)==0:
    print(-1)
else:
    ans = 1<<25
    for i in range(N):
        if S[i]:
            ans = min(ans, i-1, N-i-1)
    pre = 0
    for t in T:
        ans += 1 + (t!=pre)
        pre = t
    print(ans)
