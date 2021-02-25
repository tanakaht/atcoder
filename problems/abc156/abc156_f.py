import sys

input = sys.stdin.readline
K, Q = map(int, input().split())
D = list(map(int, input().split()))
for _ in range(Q):
    n, x, m = map(int, input().split())
    tmp = 0
    zero_cnt = 0
    for d in D:
        tmp += d % m
        zero_cnt += (d%m==0)
    cnt, rest = tmp//m, tmp%m
    tmp = x%m
    zero_cnt_tmp = 0
    n -= 1
    for d in D[:n%K]:
        tmp += d%m
        zero_cnt_tmp += (d%m==0)
    ans = n - (cnt*(n//K)) - (rest*(n//K)+tmp)//m - zero_cnt*(n//K) - zero_cnt_tmp
    print(ans)
