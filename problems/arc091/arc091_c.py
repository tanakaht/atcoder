"""
感想

- 単調減少部分列と、単調増加部分列についての性質
  - 共有する要素は高々1個
  - f(i) = |iまでの最長増加部分列|とした時、f(i)=f(j)=>iとjを並べると単調減少
  - こういうの作れば良い

/
 /
  /
   /
    /

それでいらない部分(下の方の/は一つあれば良い)を削れば良い
"""

import sys

N, A, B = map(int, input().split())

if A+B > N+1 or A*B<N:
    print(-1)
    sys.exit(0)

ans = list(range(B, 0, -1))
N -= A + B - 1
A -= 1
tmp = B
# tmpから始まって適当な数を光順で並べる
while A>0:
    tmp2 = min(N+1, B)
    for j in range(tmp+tmp2, tmp, -1):
        ans.append(j)
    tmp += tmp2
    A -= 1
    N -= tmp2-1
print(' '.join(map(str, ans)))
