N = int(input())
A = list(map(int, input().split()))
# 各操作の進む距離
A_cumsum = [0] * (N + 1)
for i in range(N):
    A_cumsum[i + 1] = A_cumsum[i] + A[i]
# 毎回終わった後にいるいち
A_cumsum_cumsum = [0] * (N + 2)
for i in range(N+1):
    A_cumsum_cumsum[i + 1] = A_cumsum_cumsum[i] + A_cumsum[i]
# 操作の中で最大の晋いち
A_cumsum_max = [0] * (N + 1)
for i in range(N):
    A_cumsum_max[i + 1] = max(A_cumsum_max[i], A_cumsum[i + 1])
max_pos = [0] * N
for i in range(N):
    max_pos[i] = A_cumsum_max[i + 1] + A_cumsum_cumsum[i + 1]
max_pos.append(A_cumsum_cumsum[-1])
print(max(max_pos))
