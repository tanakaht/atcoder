N, L = map(int, input().split())
A = sorted([L + i for i in range(N)], key=lambda x: abs(x))
print(sum(A[1:]))
