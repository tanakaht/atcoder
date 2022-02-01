import bisect

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

    def get(self, i):
        if i==0:
            return self.query(0)
        else:
            return self.query(i) - self.query(i-1)

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

N, M = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]
P = int(1e9+7)
g = [[]for _ in range(2*N)]
bit = BIT(2*N)
# edgeは低い方から高い方への有効エッジとする
# 実装上便利なので高い方から低い方へのエッジをu->v+Nって感じでやる
# まずi in [0,N]について[0, i]から出ていくedgeをカウントする
for l, r in LR:
    l -= 1
    r -= 1
    l, r = min(l, r), max(l, r)
    g[l].append(r)
    g[r].append(l+N)
    g[l+N].append(r+N)
    bit.update(l, 1)
    bit.update(r, -1)

ans = 0
for i in range(2*N):
    g[i] = sorted(g[i])

# uから(v+N以下に)出ていく本数, 端点でかぶっている分を引くために使う
def get_cnt(u, v):
    return bisect.bisect_left(g[u], v+N)

for u in range(N):
    # uから出るedgeを削除
    for v in g[u]:
        bit.update(u, -1)
        bit.update(v, 1)
    # ([u+1, v]から出ていくedge)-(vから[v+1, u+N]に出ていくedge)
    for v in g[u]:
        ans = (ans + bit.query(v)-get_cnt(v, u))%P
    # [u+1]から数えるようにアップデートする
    for v in g[u]:
        bit.update(v, 1)
        bit.update(u+N, -1)

# [(u1, v1), (u2, v2)]の入れ替え4パターンカウントしてるのでわる
print(ans//4)

# 計算量
# BIT構成: Mlog(N)
# メインループ
    # 内側のループはO(N+M)だけ回る
    # bisect, BITがlog(g[u]), log(N)
# 全体としてO((M+N)(log(M)+log(N)))なので大丈夫なはず
