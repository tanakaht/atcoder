import math


def comb(n, r):
    if n < r or r < 0:
        return 0
    nume = 1
    deno = 1
    for i in range(1, r + 1):
        nume *= (n - i + 1)
        deno *= (i)
    return nume//deno


def solve(N, K):
    if N < K:
        return 0
    if K == 0:
        return 1
    keta = math.floor(math.log(N, 10)) + 1
    x = N//pow(10, keta-1)
    ret = 0
    if K > keta:
        return 0
    # ptn1: 最大の桁は0
    if keta != K:
        ret += comb(keta - 1, K) * (9 ** K)
    # ptn2: 最大の桁はNのその桁の値未満
    ret += (x-1)*comb(keta-1, K-1)*pow(9, K-1)
    # ptn3: 最大の桁はNのその桁の値
    ret += solve(N % pow(10, keta-1), K - 1)
    return ret


N = int(input())
K = int(input())
ans = solve(N, K)
print(ans)
