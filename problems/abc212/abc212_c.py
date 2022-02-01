N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
aidx, bidx = 0, 0
ans = abs(A[0]-B[0])
for aidx in range(N):
    while bidx<M-1 and B[bidx+1]<=A[aidx]:
        bidx += 1
    ans = min(ans, abs(A[aidx]-B[bidx]))
    if bidx<M-1:
        ans = min(ans, abs(A[aidx]-B[bidx+1]))
print(ans)
