import sys

input = sys.stdin.readline
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    pi = xy[i]
    for j in range(i+1, N):
        pj = (xy[j][0]-pi[0], xy[j][1]-pi[1])
        for k in range(j+1, N):
            pk = (xy[k][0] - pi[0], xy[k][1] - pi[1])
            if pj[0] == 0 or pk[0] == 0:
                if pj[0] == 0 and pk[0] == 0:
                    print('Yes')
                    sys.exit(0)
            elif pj[1] / pj[0] == pk[1] / pk[0]:
                print('Yes')
                sys.exit(0)
print('No')
