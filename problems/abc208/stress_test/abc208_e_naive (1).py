from collections import defaultdict
N, K = map(int, input().split())
ans = 0
for i in range(1, N+1):
    tmp = 1
    if '0' in str(i):
        ans += 1
    else:
        tmp = 1
        while i:
            tmp *= i%10
            i //= 10
            if tmp>K:
                break
        ans += tmp<=K
print(ans)
