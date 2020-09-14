N = int(input())
H = list(map(int, input().split()))
ans = 0
tmp = 0
pre = -1
for h in H:
    if h <= pre:
        tmp += 1
        ans = max(ans, tmp)
    else:
        tmp = 0
    pre = h
print(ans)
