N = int(input())
ABCDE = [list(map(int, input().split())) for _ in range(N)]

def is_ok(arg):
    dp = [[[False]*(1<<5) for _ in range(N+1)] for _ in range(4)] # [0, i)みて、状態が満たせている
    dp[0][0][0] = True
    for i in range(N):
        bit = 0
        stat = ABCDE[i]
        for j in range(5):
            if stat[j] >= arg:
                bit += (1<<j)
        for j in range(4):
            for bit_ in range(1<<5):
                dp[j][i+1][bit_] = dp[j][i][bit_]
        for j in range(3):
            for bit_ in range(1<<5):
                dp[j+1][i+1][bit_|bit] |= dp[j][i][bit_]
    return dp[-1][-1][-1]


def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(bisect(int(1e9)+2, 0))
