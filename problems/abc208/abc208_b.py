P = int(input())
ans = 0
tmp = 1
for i in range(10, 0, -1):
    tmp *= i
for i in range(10, 0, -1):
    ans += P//tmp
    P %= tmp
    tmp //= i
print(ans)
