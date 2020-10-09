from collections import Counter

S = list(map(int, input()))[::-1]
P = 2019
S_i = [0]*(len(S)+1)
for i, s in enumerate(S):
    S_i[i + 1] = (S_i[i] + pow(10, i, P) * s) % P
c = Counter(S_i)
ans = 0
for k, cnt in c.items():
    ans += cnt * (cnt - 1) // 2
print(ans)
