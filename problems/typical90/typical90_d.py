H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
hs = [0]*H
ws = [0]*W
for h in range(H):
    for w in range(W):
        hs[h] += A[h][w]
        ws[w] += A[h][w]
B = [[0]*W for _ in range(H)]
for h in range(H):
    for w in range(W):
        B[h][w] = hs[h]+ws[w]-A[h][w]
    print(*B[h])
