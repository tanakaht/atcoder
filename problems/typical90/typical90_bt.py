H, W = map(int, input().split())
C = [list(map(lambda x: x=='#', input())) for _ in range(H)]
xy2idx = lambda x, y: x*W+y
state2idx = lambda x, y, start_x, start_y, bit: xy2idx(x, y)*(1<<(H*W))*H*W+xy2idx(start_x, start_y)*(1<<(H*W))+bit
def idx2state(idx):
    xy = idx//((1<<(H*W))*H*W)
    x, y = xy//W, xy%W
    start_xy = (idx//(1<<(H*W)))%(H*W)
    start_x, start_y = start_xy//W, start_xy%W
    bit = idx%(1<<(H*W))
    return (x, y, start_x, start_y, bit)
q = []
appeared = [False]*((1<<(H*W))*H*W*H*W)
for x in range(H):
    for y in range(W):
        if not C[x][y]:
            idx = state2idx(x, y, x, y, 1<<(xy2idx(x, y)))
            q.append(idx)
ans = -1
while q:
    u = q.pop()
    if appeared[u]:
        continue
    appeared[u] = True
    x, y, start_x, start_y, bit = idx2state(u)
    # 探索先を追加
    for x_d, y_d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x_, y_ = x+x_d, y+y_d
        if not (0<=x_<H and 0<=y_<W):
            continue
        if C[x_][y_]:
            continue
        if x_==start_x and y==start_y:
            ans_ = bin(bit).count('1')
            if ans_>=3:
                ans = max(ans, ans_)
        bit_ = bit|(1<<xy2idx(x_, y_))
        if bit==bit_:
            continue
        v = state2idx(x_, y_, start_x, start_y, bit_)
        if not appeared[v]:
            q.append(v)
print(ans)
