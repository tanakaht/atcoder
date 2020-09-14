N, K, M = map(int, input().split())
A = list(map(int, input().split()))
A_sum = sum(A)
if M*N - A_sum > K:
    print(-1)
else:
    print(max(0, M*N-A_sum))
