N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
if A[-M] >= sum(A) / (4 * M):
    print('Yes')
else:
    print('No')
