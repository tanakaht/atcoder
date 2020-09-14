N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
d1, d2, d3, d4 = [[] for _ in range(4)]
for a, b in xy:
    d1.append(a + b)
    d2.append(a - b)
    d3.append(-a + b)
    d4.append(-a - b)
ans = 0
for d in d1, d2, d3, d4:
    ans = max(ans, max(d) - min(d))
print(ans)
