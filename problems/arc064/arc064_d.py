import math
N, K = map(int, input().split())
P = int(1e9+7)
ans = (pow(K, math.ceil(N/2), P)*N)%P
for i in range(N):
