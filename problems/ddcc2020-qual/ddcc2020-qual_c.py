import sys

input = sys.stdin.readline
H, W, K = map(int, input().split())
S = [list(map(lambda x: x=='#', input())) for _ in range(H)]
ans = [[0]*W for _ in range(H)]
h_q = []
last_h = None
piece_n = 1
for h in range(H):
    if sum(S[h])==0:
        h_q.append(h)
        continue
    w_q = []
    for w in range(W):
        w_q.append(w)
        if S[h][w]:
            while w_q:
                w_ = w_q.pop()
                ans[h][w_] = piece_n
            piece_n += 1
    while w_q:
        w_ = w_q.pop()
        ans[h][w_] = piece_n - 1
    while h_q:
        h_ = h_q.pop()
        ans[h_] = ans[h]
    last_h = h
while h_q:
    h_ = h_q.pop()
    ans[h_] = ans[last_h]
for h in range(H):
    print(' '.join(map(str, ans[h])))

