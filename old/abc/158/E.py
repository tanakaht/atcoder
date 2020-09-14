import collections, sys
N, P = map(int, input().split())
S = input()
s_mod = [0]*(N+1)

ans = 0
if P == 2:
    for i in range(N):
        ans += ((int(S[-(i+1)])%2) ^ 1) * (N-i)
    print(ans)
    sys.exit()
elif P == 5:
    for i in range(N):
        ans += ((int(S[-(i + 1)]) % 5) == 0) * (N - i)
    print(ans)
    sys.exit()


for i in range(N):
    s_mod[i+1] = (pow(10, i, P) * int(S[-(i+1)])+s_mod[i]) % P
c = collections.Counter(s_mod)
for v in c.values():
    ans = (ans + v*(v-1)//2)
print(ans)
