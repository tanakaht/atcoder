H = int(input())
ans = 0
i = 1
while H >= 1:
    ans += i
    i *= 2
    H //= 2
print(ans)
