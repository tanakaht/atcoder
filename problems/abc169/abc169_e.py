N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A = sorted(A)
B = sorted(B)
if N % 2 == 1:
    ans = B[(N - 1) // 2] - A[(N - 1) // 2] + 1
    print(ans)
else:
    ans = B[N // 2 - 1] + B[N // 2] - (A[N // 2 - 1] + A[N // 2]) + 1
    print(ans)
