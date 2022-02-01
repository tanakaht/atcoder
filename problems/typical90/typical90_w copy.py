from collections import defaultdict

H, W = map(int, input().split())
is_black = [list(map(lambda x: x=='#', input())) for _ in range(H)]
P = int(1e9)+7

bit2id = {}
cur_id = 0
g = defaultdict(list) # [[] for _ in range(121393)]  # defaultdict(list)
has_nth_bit_list = [[] for _ in range(W)]
# このループで5~6秒
for bit in range(1<<W):
    flg = not ((bit>>0)&1 and (bit>>(1))&1)
    for i in range(1, W):
        if (bit>>i)&1 and ((bit>>(i-1))&1 or (bit>>(i+1))&1):
            flg = False
    if flg:
        bit2id[bit] = cur_id
        for i in range(W):
            if (bit>>i)&1:
                has_nth_bit_list[i].append(cur_id)
        cur_id += 1
        u_bit = bit
        d_bit = bit^u_bit
        # 3^(n_state)回る一番重いとこ
        while u_bit>0:
            g[bit2id[u_bit]].append(bit2id[d_bit])
            u_bit = (u_bit-1)&bit
            d_bit = u_bit^bit
        g[bit2id[u_bit]].append(bit2id[d_bit])
g = [g[i] for i in g.keys()]
n_state = len(bit2id.keys())
dp = [0]*n_state
dp[bit2id[0]] = 1
for h in range(H):
    new_dp = [0]*n_state
    for i in range(n_state):
        v = dp[i]
        # 3^(n_state)回る
        for j in g[i]:
            new_dp[j] = (new_dp[j]+v)%P
    for w in range(W):
        if is_black[h][w]:
            for i in has_nth_bit_list[w]:
                new_dp[i] = 0
    dp = new_dp
ans = 0
for i in dp:
    ans = (ans+i)%P
print(ans)
