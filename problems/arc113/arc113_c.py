from collections import defaultdict
S = input()[::-1]
d = defaultdict(int)
pre = None
ans = 0
cnt = 0
for i in range(len(S)):
    if pre == S[i]:
        ans += i - d[S[i]]
        d = defaultdict(int)
        d[S[i]] = i+1
    else:
        d[S[i]] += 1
    pre = S[i]
print(ans)
