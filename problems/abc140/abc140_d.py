N, K = map(int, input().split())
S = list(input())

cnt = 0
init_s = S[0]
pre = '_'
for i, s in enumerate(S):
    if s != init_s:
        if pre != s:
            K -= 1
        if K == -1:
            break
        S[i] = init_s
    pre = s
ans = 0
pre = '_'
for s in S:
    ans += pre == s
    pre = s
print(ans)
