N = int(input())
W = list(map(int, input().split()))
t2 = sum(W)
t1 = 0
ans = t2
for w in W:
    t1 += w
    t2 -= w
    ans = min(ans, abs(t1 - t2))
print(ans)
