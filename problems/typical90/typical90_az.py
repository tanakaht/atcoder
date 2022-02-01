N = int(input())
As = [list(map(int, input().split())) for _ in range(N)]
MOD = int(1e9+7)
ans = 1
for A in  As:
    ans = (ans*sum(A))%MOD
print(ans)
