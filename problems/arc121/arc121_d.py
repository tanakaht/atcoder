import math
N = int(input())
A = sorted(list(map(int, input().split())))
Am, Ap = [], []
for a in A:
  if a<0:
    Am.append(a)
  else:
    Ap.append(a)
ans = math.inf
for i in range(N+1):
  if (N+i)%2!=0:
    continue
  Atmp = Am+([0]*i)+Ap
  X, Y = -math.inf, math.inf
  for j in range(len(Atmp)//2):
    X = max(X, Atmp[j]+Atmp[-j-1])
    Y = min(Y, Atmp[j]+Atmp[-j-1])
  ans = min(ans, X-Y)
print(ans)
