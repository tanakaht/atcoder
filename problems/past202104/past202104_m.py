from collections import defaultdict

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

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
Qs = [list(map(int, input().split())) for _ in range(Q)]
v_count = defaultdict(int)
event_in = [None]*(N) # 値、出るとこ
event_out = [None]*(N) # 値, 入るとこ
event_cnt = BIT(N)

ans = 0
for i, v in enumerate(A):
    event_in[i] = (v, i)
    event_out[i] = (v, i)
    event_cnt.update(i, 2)
    ans -= max(0, v_count[v]*(v_count[v]-1)//2)
    v_count[v] += 1
    ans += max(0, v_count[v]*(v_count[v]-1)//2)
for l, r, x in Qs:
    l -= 1
    r -= 1

    # [l, r]を消す
    while event_cnt.query(r) - event_cnt.query(l-1):
        idx = event_cnt.lower_left(event_cnt.query(l-1)+1)
        if event_in[idx] is not None:
            v, i = event_in[idx]
            # 削除
            if i<=r:
                ans -= max(0, v_count[v]*(v_count[v]-1)//2)
                v_count[v] -= i-idx+1
                ans += max(0, v_count[v]*(v_count[v]-1)//2)
                event_in[idx] = None
                event_out[i] = None
                event_cnt.update(idx, -1)
                event_cnt.update(i, -1)
            # スライド
            else:
                ans -= max(0, v_count[v]*(v_count[v]-1)//2)
                v_count[v] -= r-idx+1
                ans += max(0, v_count[v]*(v_count[v]-1)//2)
                event_in[idx] = None
                event_in[r+1] = (v, i)
                event_out[i] = (v, r+1)
                event_cnt.update(idx, -1)
                event_cnt.update(r+1, 1)

        if event_out[idx] is not None:
            v, i = event_out[idx]
            # 削除
            if i>=l:
                ans -= max(0, v_count[v]*(v_count[v]-1)//2)
                v_count[v] -= idx-i+1
                ans += max(0, v_count[v]*(v_count[v]-1)//2)
                event_out[idx] = None
                event_in[i] = None
                event_cnt.update(idx, -1)
                event_cnt.update(i, -1)
            # スライド
            else:
                ans -= max(0, v_count[v]*(v_count[v]-1)//2)
                v_count[v] -= idx-l+1
                ans += max(0, v_count[v]*(v_count[v]-1)//2)
                event_out[idx] = None
                event_out[l-1] = (v, i)
                event_in[i] = (v, l-1)
                event_cnt.update(idx, -1)
                event_cnt.update(l-1, 1)
    # [l, r]を含んでいたら左右に分割
    idx = event_cnt.lower_left(event_cnt.query(l-1))
    if event_in[idx] is not None and event_in[idx][1]>=r:
        v, i = event_in[idx]
        event_in[idx] = (v, l-1)
        event_out[l-1] = (v, idx)
        event_in[r+1] = (v, i)
        event_out[i] = (v, r+1)
        ans -= max(0, v_count[v]*(v_count[v]-1)//2)
        v_count[v] -= r-l+1
        ans += max(0, v_count[v]*(v_count[v]-1)//2)
        event_cnt.update(l-1, 1)
        event_cnt.update(r+1, 1)
    ans -= v_count[x]*(v_count[x]-1)//2
    v_count[x] += r-l+1
    ans += v_count[x]*(v_count[x]-1)//2
    event_in[l] = (x, r)
    event_out[r] = (x, l)
    event_cnt.update(l, 1)
    event_cnt.update(r, 1)
    print(ans)
