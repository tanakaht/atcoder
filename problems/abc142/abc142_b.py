N, K = map(int, input().split())
H = list(map(int, input().split()))
ans = 0
for h in H:
    ans += h >= K
print(ans)
