import itertools

N = int(input())
As = []
xys = []
for _ in range(N):
    a = int(input())
    As.append(a)
    xys.append([tuple(map(int, input().split())) for _ in range(a)])


ans = -1
for is_shoziki in itertools.product([1, 0], repeat=N):
    n = sum(is_shoziki)
    if n <= ans:
        continue
    flg = True
    for i in range(N):
        if not flg:
            break
        if is_shoziki[i] == 0:
            continue
        for x, y in xys[i]:
            if is_shoziki[x - 1] != y:
                flg = False
                break
    if flg:
        ans = n

print(ans)
