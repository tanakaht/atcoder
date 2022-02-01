import math
N = int(input())
MOD =998244353
ans = 0
def is_ok(x, z):
    return 0<=(x**2-z**2)<=N and x<=N

def bisect(ng, ok, z):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, z):
            ok = mid
        else:
            ng = mid
    return ok
# x^2-y=z^2
# (x-z)(x+z)=y
# t=(x-z)としてtを全探索(root(N))まででよし
for t in range(1, int(math.sqrt(N))+1):
    fr_, to_ = t, N//t
    if fr_>to_:
        break
    else:
        ans = (ans+(to_-fr_)//2+1)%MOD
print(ans)
