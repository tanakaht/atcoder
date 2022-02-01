S, K = input().split()
K = int(K)
P = 998244353
l = []
one_cnt = 0
for s in S[::-1]:
    if s == '0':
        l.append(one_cnt)
        one_cnt = 0
    else:
        one_cnt += 1
l.append(one_cnt)
dp = [[0]*len(S) for _ in range(len(l)+1)] # (右からi番目の0までみて, そこからjこの1を集めた)=>パターン数
dp[0][0] = 1
for i in range(len(l)):
    #もらうパターン
    for j in range(len(S)):
