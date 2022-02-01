N, D, H = map(int, input().split())
dhs = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for d, h in dhs:
    x = (D*h-d*H)/(D-d)
    ans = max(ans, x)
print(ans)
