N, M = map(int, input().split())
A = list(map(int, input().split()))
P = 998244353
# 再利用する時あらかじめN以下の計算しとく
kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, N+2):
    tmp = (tmp*i) % P
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, P - 2, P))

def comb(n, r):
    if n < r or n < 0:
        return 0
    elif n == r or r==0:
        return 1
    else:
        return (((kaizyo[n] * kaizyo_inv[r])%P) * kaizyo_inv[n - r])%P

dp = [[None]*(N+1) for _ in range(M+1)] # a回操作, あとb個揃える
def cnt_ptn(a, b):
    if dp[a][b] is not None:
        return dp[a][b]
    if a == b:
        ret = 1
    elif a<b or (b==0 and a>0):
        ret = 0
    else:
        ret = (2*b*cnt_ptn(a-1, b) + cnt_ptn(a-1, b-1))%P
    dp[a][b] = ret
    return ret

for a in range(M+1):
    for b in range(N+1):
        cnt_ptn(a, b)

# [0, l)は左から揃え、(r, N-1]は右から揃える
def solve(l, r):
    c = l + (N-1-r)
    if c > M:
        return 0
    ret = (comb(c, l) * cnt_ptn(M, c))%P
    return ret

ans = 0
for l in range(N+1):
    r = l - 1
    ans = (ans+solve(l, r))%P
    pre = -1
    while r<N-1 and A[r+1] > pre:
        r += 1
        tmp = solve(l, r)
        ans = (ans+solve(l, r))%P
        pre = A[r]
print(ans)
