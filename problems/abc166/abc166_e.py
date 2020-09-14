from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
Ai = [(i + 1) - a for i, a in enumerate(A)]
Aj = [(j + 1) + a for j, a in enumerate(A)]
cntAi = defaultdict(lambda: 0)
for ai in Ai:
    cntAi[ai] += 1

ans = 0
for ai, aj in zip(Ai, Aj):
    cntAi[ai] -= 1
    ans += cntAi[aj]
print(ans)
