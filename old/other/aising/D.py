import sys
N = int(input())
X = int(input(), 2)
x_popcount = sum(map(int, bin(X)[2:]))
is_zeroflg = [x_popcount-1 <= 0, False]
x_popcounts = [max(1, x_popcount - 1), x_popcount + 1]
X_per_popcounts = [X % x_popcounts[0], X % x_popcounts[1]]
mods = [0, 0]
ans = [0]*N


def f(n):
    cnt = 0
    while n != 0:
        popcount = sum(map(int, bin(n)[2:]))
        n = n % popcount
        cnt += 1
    return cnt


flg = X & 1 ^ 1
mods[0] = (-1) % x_popcounts[0]
mods[1] = 1 % x_popcounts[1]
tmp = (X_per_popcounts[flg] + mods[flg]) % x_popcounts[flg]
ans[0] = f(tmp) + 1
if is_zeroflg[flg]:
    ans[0] = 0

for i in range(1, N):
    flg = (X >> i) & 1 ^ 1
    mods[0] = (mods[0] * 2) % (x_popcounts[0])
    mods[1] = (mods[1] * 2) % (x_popcounts[1])
    tmp = (X_per_popcounts[flg] + mods[flg]) % x_popcounts[flg]
    ans[i] = f(tmp) + 1
    if is_zeroflg[flg]:
        ans[i] = 0

print('\n'.join(map(str, ans[::-1])))
