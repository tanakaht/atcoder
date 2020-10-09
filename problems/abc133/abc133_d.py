N = int(input())
A = list(map(int, input().split()))
ans = [0] * N
tmp = 0
for i, a in enumerate(A[:-1]):
    tmp -= pow(-1, i) * a
ans[0] = (A[-1] - tmp) // 2
for i in range(1, N):
    ans[i] = A[i - 1] - ans[i - 1]
print(' '.join(map(lambda x: str(x*2), ans)))
