n = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(1, n - 1):
    ans += p[i] == sorted(p[i - 1:i + 2])[1]
print(ans)
