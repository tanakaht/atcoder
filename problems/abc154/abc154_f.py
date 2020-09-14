import math

r1, c1, r2, c2 = map(int, input().split())
P = int(1e9+7)
kaizyo = [0]
kaizyo_inv = [0]
tmp = 1
for i in range(1, 2*max(r1, r2, c1, c2)+2):
    tmp = (tmp*i) % P
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, P - 2, P))


def comb(n, r):
    if n < r or n == 0:
        return 0
    elif n == r or r == 0:
        return 1
    else:
        return kaizyo[n] * kaizyo_inv[r] * kaizyo_inv[n - r]


def solve_naive(r, c):
    if r < 0 or c < 0:
        return 0
    S = [[0] * (c+1) for _ in range(r+1)]
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            S[i][j] = S[i - 1][j] + S[i][j - 1] - \
                S[i - 1][j - 1] + comb(i + j, i)
    return S[-1][-1]


def solve(r, c):
    if r < 0 or c < 0:
        return 0
    ret = 0
    for i in range(2, r + 2):
        ret = (ret + comb(i + c, i)) % P
    return ret


# solve = solve_naive
ans = (solve(r2, c2) - solve(r1 - 1, c2) -
       solve(r2, c1 - 1) + solve(r1 - 1, c1 - 1)) % P
print(ans)
