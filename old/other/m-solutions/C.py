N, K = map(int, input().split())
A = list(map(int, input().split()))

for ai_k, ai in zip(A, A[K:]):
    print('Yes' if ai_k < ai else 'No')
