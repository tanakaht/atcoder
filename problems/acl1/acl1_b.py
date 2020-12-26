"""
感想
- O(sqrt(N))くらいでやりたい
  - 試してみたらpow(2, 素因数の数)はいけた=>なんで？=>高々約数個で抑えられるのでO(sqrt(N))
  - sum(1+...+k)=k*(k+1)/2なので2Nの各素因数についてmodで0or-1が成り立つ, これ全部探索してもO(sqrt(N))
  - 中国剰余定理で1~Nの範囲で回を求めて全探索した最小を返す(素因数の数はO(log(N)))
- crtとextgcdの勉強になった
- pow(a, -1, mod)はPythonにはあるけどPyPyにはない
"""
import math
from math import gcd

def extgcd(a, b):
    """
    d=gcd(a, b)として
    ax + by = dになるd, x, yを返す
    """
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

def crt(eqs):
    """
    eqs: rest, mod のlist
    """
    ret = eqs[0][0]%eqs[0][1]
    mods = eqs[0][1]
    for rest, mod_ in eqs[1:]:
        d, x, y = extgcd(mods, mod_)
        if d != 1:
            raise ValueError('互いに素でない')
        ret = (mods*x*rest + mod_*y*ret) % (mods*mod_)
        mods *= mod_
    return ret

N = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

factors = factorization(2 * N)
ans = N
for bitflg in range(pow(2, len(factors))):
    eqs = []
    for i, (f, cnt) in enumerate(factors):
        b = bitflg>>i & 1
        eqs.append((-1+int(b), pow(f, cnt)))
    tmp = crt(eqs)
    if tmp != 0:
        ans = min(ans, crt(eqs))
print(ans)
