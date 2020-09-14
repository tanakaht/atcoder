import sys
input = sys.stdin.readline
N, M = map(int, input().split())
scs = sorted([tuple(map(int, input().split())) for _ in range(M)])
ans = ['0'] * N

if M == 0:
    if N != 1:
        ans[0] = '1'
    print(''.join(ans))
    sys.exit()

if scs[0][0] != 1:
    if N != 1:
        ans[0] = '1'

for s, c in scs:
    if ans[s-1] != '0' and ans[s-1] != str(c):
        print(-1)
        sys.exit()
    else:
        ans[s-1] = str(c)

if ans[0] == '0' and N != 1:
    print(-1)
else:
    print(''.join(ans))