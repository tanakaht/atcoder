import sys
from collections import deque

input = sys.stdin.readline
class BIT:
    def __init__(self,len_A):
        self.N = len_A + 10
        self.bit = [0]*(len_A+10)

    # sum(A0 ~ Ai)
    # O(log N)
    def query(self,i):
        res = 0
        idx = i+1
        while idx:
            res += self.bit[idx]
            idx -= idx&(-idx)
        return res

    # Ai += x
    # O(log N)
    def update(self,i,x):
        idx = i+1
        while idx < self.N:
            self.bit[idx] += x
            idx += idx&(-idx)

    # min_i satisfying {sum(A0 ~ Ai) >= w} (Ai >= 0)
    # O(log N)
    def lower_left(self,w):
        if (w < 0):
            return -1
        x = 0
        k = 1<<(self.N.bit_length()-1)
        while k > 0:
            if x+k < self.N and self.bit[x+k] < w:
                w -= self.bit[x+k]
                x += k
            k //= 2
        return x

H, W, M = map(int, input().split())
M_Hs = [W]*H
M_Ws = [H]*W
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    M_Hs[x] = min([M_Hs[x], y])
    M_Ws[y] = min([M_Ws[y], x])
bit = BIT(H+1)
for h in range(H):
    bit.update(h, 1)
ans = 0
evq = [] # 封鎖が, どこまで
for h in range(M_Ws[0]):
    bit.update(h, -1)
    ans += M_Hs[h]
    evq.append((h, M_Hs[h]))

evq = deque(sorted(evq, key=lambda x: x[1]))
for w in range(M_Hs[0]):
    while len(evq) > 0 and evq[0][1] < w:
        h, _ = evq.popleft()
        bit.update(h, 1)
    ans += bit.query(M_Ws[w]-1)
print(ans)
