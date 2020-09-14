import math

S = input()
T = input()
ans = math.inf
for i in range(len(S) - len(T)+1):
    tmp = sum([s != t for s, t in zip(S[i:i + len(T)], T)])
    ans = min(ans, tmp)
print(ans)
