import math
import heapq

H, W = map(int, input().split())
M = [list(map(int, input())) for _ in range(H)]
d_d = {2: [(4, 1), (1, 3), (3, 6), (6, 4)],
       5: [(4, 6), (6, 3), (3, 1), (1, 4)],
       1: [(4, 5), (5, 3), (3, 2), (2, 4)],
       6: [(4, 2), (2, 3), (3, 5), (5, 4)],
       4: [(6, 5), (5, 1), (1, 2), (2, 6)],
       3: [(6, 2), (2, 1), (1, 5), (5, 6)]
        }
def transition(state, dir):
    if dir == 'u':
        for k, v in d_d.items():
            if state in v:
                return (7-k, state[1])
    elif dir == 'd':
        for k, v in d_d.items():
            if state in v:
                return (k, state[1])
    elif dir == 'l':
        return (state[1], 7-state[0])
    elif dir == 'r':
        return (7-state[1], state[0])

dp = [[[[math.inf]*W for _ in range(H)] for _ in range(7)] for _ in range(7)] # 上のめ,したのめ,場所=>最小コスト
dp[1][3][0][0] = 0
q = [(0, (0, 0), (1, 3))] # cost, 場所, 目の状態
while q:
    c, (h, w), state = heapq.heappop(q)
    if h == H-1 and w==W-1:
        print(c)
        break
    for dir in 'udlr':
        h_, w_ = h, w
        if dir == 'u':
            h_ -= 1
        elif dir == 'd':
            h_ += 1
        elif dir == 'l':
            w_ -= 1
        elif dir == 'r':
            w_ += 1
        if not (0<=h_<H and 0<=w_<W):
            continue
        state_ = transition(state, dir)
        c_ = c+abs(M[h_][w_]-state_[0])
        if dp[state_[0]][state_[1]][h_][w_] > c_:
            dp[state_[0]][state_[1]][h_][w_] = c_
            heapq.heappush(q, (c_, (h_, w_), state_))
