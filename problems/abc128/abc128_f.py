import sys

N = int(input())
S = list(map(int, input().split()))
ans = 0
for y in range(1, N+1):
    appeared = set()
    i = 0
    pre = 0
    while i*y<N-1-y and i*y not in appeared and N-1-i*y not in appeared and N-1!=2*i*y:
        pre += S[i*y]+S[N-1-i*y]
        ans = max(ans, pre)
        appeared.add(i*y)
        appeared.add(N-1-i*y)
        i += 1
print(ans)
