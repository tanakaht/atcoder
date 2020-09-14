A, B, K = map(int, input().split())
taka = max(0, A - K)
aoki = max(0, B - max(0, K - A))
print(taka, aoki)
