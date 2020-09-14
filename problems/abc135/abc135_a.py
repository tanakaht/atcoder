A, B = map(int, input().split())
K = (A + B) // 2
if abs(A - K) == abs(K - B):
    print(K)
else:
    print('IMPOSSIBLE')
