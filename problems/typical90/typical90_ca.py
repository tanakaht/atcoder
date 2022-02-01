import sys

input = sys.stdin.readline
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
ans = 0
for h in range(H):
    for w in range(W):
        if w==W-1 or h==H-1:
            if A[h][w]!=B[h][w]:
                print('No')
                sys.exit(0)
        else:
            diff = B[h][w]-A[h][w]
            ans += abs(diff)
            A[h][w] += diff
            A[h+1][w] += diff
            A[h][w+1] += diff
            A[h+1][w+1] += diff

print('Yes')
print(ans)
