import sys
import heapq


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

    def get(self, i):
        return self.query(i)-self.query(i-1)

class CppLikeSet:
    def __init__(self, available):
        available = sorted(set(available))
        self.N = len(available)
        self.value2idx = {v: i for i, v in enumerate(available)}
        self.idx2value = {i: v for v, i in self.value2idx.items()}
        self.bit = BIT(len(self.value2idx))

    def add(self, v):
        idx = self.value2idx[v]
        self.bit.update(idx, 1)

    def remove(self, v):
        idx = self.value2idx[v]
        assert self.bit.get(idx)>0, f"{v} not found"
        self.bit.update(idx, -1)

    # i番目の要素を取得(0-indexed)
    def get(self, i):
        assert self.bit.query(self.N)>=i
        i+=1
        ng, ok = -1, self.N
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if self.bit.query(mid)>=i:
                ok = mid
            else:
                ng = mid
        return self.idx2value[ok]

    # v以上の最小の値
    def upper_bound(self, v):
        i = self.bit.query(self.value2idx[v])+1
        return self.get(i)

    # v以下の最大の値
    def lower_bound(self, v):
        i = self.bit.query(self.value2idx[v])-self.bit.get(self.value2idx[v])
        return self.get(i)

    # vは何番目の要素?
    def get_idx(self, v):
        return self.bit.query(self.value2idx[v])  # 右端
        # return self.bit.query(self.value2idx[v]-1)+1  # 左端


input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
UV = [list(map(int, input().split())) for _ in range(N-1)]
g=[[] for _ in range(N)]
for u, v in UV:
    g[u-1].append(v-1)
    g[v-1].append(u-1)

children = [[] for _ in range(N)]
parents = [None]*N
q = [(0, None)]
while len(q) > 0:
    v, p = q.pop()
    parents[v] = p
    for u in g[v]:
        if u != p:
            q.append((u, v))
            children[v].append(u)


dp = [None]*N  # その頂点を踏んだ時の中央値
depth = [None]*N
q = [~0, 0]
med = CppLikeSet(set(A))
dfs_ord = []
cnt = 0
while q:
    u = q.pop()
    if u >= 0:
        # 行きがけの処理
        med.add(A[u])
        cnt += 1
        depth[u] = cnt
        # 記録
        dfs_ord.append(u)
        # 探索先を追加
        for v in children[u][::-1]:
            q.append(~v)
            q.append(v)
        if not children[u]:
            # 中央値をメモ
            if cnt%2==1:
                dp[u] = med.get(cnt//2)
            else:
                dp[u] = (med.get(cnt//2)+med.get(cnt//2-1))//2
    else:
        # 帰りがけの処理
        med.remove(A[~u])
        cnt -= 1

def dfs(u):
    if dp[u] is not None:
        return dp[u]
    vals = []
    for v in children[u]:
        vals.append(dfs(v))
    ret = max(vals) if depth[u]%2 else min(vals)
    dp[u] = ret
    return dp[u]

for u in dfs_ord[::-1]:
    dfs(u)
print(dp[0])
