N = int(input())
X = list(map(int, input().split()))
ans = 0
for x in X:
    ans += abs(x)
print(ans)

ans = 0
for x in X:
    ans += abs(x)**2
print(ans**0.5)

ans = 0
for x in X:
    ans = max(ans, abs(x))
print(ans)
