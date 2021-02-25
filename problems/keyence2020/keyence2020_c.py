N, K, S = map(int, input().split())
if S==int(1e9):
    A = [1]*N
else:
    A = [int(1e9)]*N
for i in range(K):
    A[i] = S
print(' '.join(map(str, A)))
