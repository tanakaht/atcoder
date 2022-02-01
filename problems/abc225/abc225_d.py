import sys

N, Q = map(int, input().split())
train = [[None, None] for _ in range(N)]
for _ in range(Q):
    query = input().split()
    flg = int(query[0])
    if flg==1:
        x, y = map(int, query[1:])
        x -= 1
        y -= 1
        train[x][1] = y
        train[y][0] = x
    elif flg==2:
        x, y = map(int, query[1:])
        x -= 1
        y -= 1
        train[x][1] = None
        train[y][0] = None
    elif flg==3:
        x = int(query[1])
        x -= 1
        while train[x][0] is not None:
            x = train[x][0]
        ans = [x+1]
        while train[x][1] is not None:
            x = train[x][1]
            ans.append(x+1)
        print(len(ans), *ans)
