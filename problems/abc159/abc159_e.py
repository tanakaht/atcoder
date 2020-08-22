import math
H, W, K = map(int, input().split())
S = [list(map(lambda x: int(x=='1'), input())) for _ in range(H)]


def cal_min_vert_div(hs):
    cnt = 0
    n_h_div = len(hs)
    n_white = [0]*n_h_div
    for i in range(W):
        for j in range(n_h_div):
            n_white[j] += hs[j][i]
            if n_white[j] > K:
                n_white = [hs[k][i] for k in range(n_h_div)]
                cnt += 1
                if max(n_white)>K:
                    return math.inf
                break
    return cnt

ans = math.inf

for mask in range(2**(H-1)):
    hs = []
    tmp = S[0]
    for i in range(H-1):
        if mask>>i & 1:
            hs.append(tmp)
            tmp = S[i+1]
        else:
            tmp = [tmp[w]+S[i+1][w] for w in range(W)]
    hs.append(tmp)
    tmp = cal_min_vert_div(hs)+sum(map(int, bin(mask)[2:]))
    ans = min(ans, tmp)
print(ans)



