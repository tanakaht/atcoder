N = int(input())
ans = 0
for i in range(1, N+1):
    flg = True
    tmp = i
    while tmp > 0:
        if tmp % 10 == 7:
            flg = False
        tmp //= 10
    tmp = i
    while tmp > 0:
        if tmp % 8 == 7:
            flg = False
        tmp //= 8
    ans += flg

print(ans)
