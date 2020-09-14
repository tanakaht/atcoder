N, K = map(int, input().split())

ans = 0
div = K
while N/pow(K, ans) >= 1:
    ans += 1
    div *= ans
print(ans)
