def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    return arr

N = int(input())
ans = 0
for _, cnt in factorization(N):
    i = 1
    while i<=cnt:
        ans += 1
        cnt -= i
        i += 1

print(ans)