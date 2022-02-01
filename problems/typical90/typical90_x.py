N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for a, b in zip(A, B):
    K -= abs(a-b)
if K>=0 and K%2==0:
    print('Yes')
else:
    print('No')
