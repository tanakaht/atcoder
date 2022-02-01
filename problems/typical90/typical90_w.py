from collections import defaultdict
import time
ts=time.time()
H, W = map(int, input().split())
is_black = [list(map(lambda x: x=='#', input())) for _ in range(H)]
mod = int(1e9)+7

bit2id = [{} for _ in range(W)] # w=iの位置でありうるbitのid
cur_id = 0
for w in range(W):
    cur_id = 0
    for bit in range(1<<(W+1)):
        if w==0:
            if bit&1:
                if bit>>(W-1):
                    continue
            if (bit>>1)&(bit>>2):
                continue
        elif w==1:
            if bit>>W:
                if bit%(1<<2):
                    continue
                bit_ = bit-(1<<W)
                if (bit_)&(bit_>>1):
                    continue
            elif (bit)&(bit>>1):
                continue
        else:
            pre, aft = bit%(1<<(W-w+1)), bit//(1<<(W-w+1))
            if pre&(pre>>1):
                continue
            if aft&(aft>>1):
                continue
            if (bit>>W) and bit%(1<<2):
                continue
            elif (bit&1) and bit//(1<<(W-1)):
                continue
        bit2id[w][bit] = cur_id
        cur_id += 1
print(time.time()-ts)
g = [[[] for _ in range(len(bit2id[w].keys()))] for w in range(W)]
for w in range(W):
    cur_id = 0
    bit2idfr = bit2id[w]
    bit2idto = bit2id[(w+1)%W]
    for bit in bit2idfr.keys():
        bit_ = bit>>1
        g[w][bit2idfr[bit]].append(bit2idto[bit_])
        try:
            bit_ = (bit>>1) + (1<<W)
            if w==0 or (not bit&1):
                g[w][bit2idfr[bit]].append(bit2idto[bit_])
        except KeyError:
            pass
print(time.time()-ts)
dp = [0]*len(bit2id[0].keys())
dp[bit2id[0][0]] = 1
cnt = 0
for h in range(H):
    for w in range(W):
        new_dp = [0]*len(g[(w+1)%W])
        for i in range(len(g[w])):
            if is_black[h][w]:
                for j in g[w][i][:1]:
                    new_dp[j] = (new_dp[j]+dp[i])%mod
            else:
                for j in g[w][i]:
                    new_dp[j] = (new_dp[j]+dp[i])%mod
        dp = new_dp
print(time.time()-ts)
ans = 0
for i in dp:
    ans = (ans+i)%mod
print(ans)
