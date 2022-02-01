import sys

N = int(input())
S = input()
T = input()
if S.count('0')!=T.count('0'):
    print(-1)
    sys.exit(0)

ans = S.count('0')
scnt = 0
tcnt = 0
for s, t in zip(S, T):
    if s=="0":
        scnt += 1
    if t == "0":
        tcnt += 1
    if s=='0' and t=='0':
        ans -= scnt==tcnt
print(ans)
