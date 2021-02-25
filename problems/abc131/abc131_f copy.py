from collections import defaultdict

N = int(input())
XY = []
Xs = defaultdict(set)
Ys = defaultdict(set)
for _ in range(N):
    x, y = map(int, input().split())
    Xs[x].add(y)
    Ys[y].add(x)
    XY.append((x, y))

X_appeared = defaultdict(lambda: False)
Y_appeared = defaultdict(lambda: False)
cnt = 0
for x, y in XY:
    if X_appeared[x] or Y_appeared[y]:
        continue
    if len(Xs[x]) >= 2 and len(Ys[y]) >= 2:
        xs, ys = set(Ys[y]), set(Xs[x])
        xq = list(Ys[y])
        yq = list(Xs[x])
        while xq or yq:
            if xq:
                p = xq.pop()
                for y_ in Xs[p]:
                    if y_ not in ys:
                        ys.add(y_)
                        yq.append(y_)
            if yq:
                p = yq.pop()
                for x_ in Ys[p]:
                    if x_ not in xs:
                        xs.add(x_)
                        xq.append(x_)
        cnt += len(xs)*len(ys)
        for x_ in xs:
            X_appeared[x_] = True
        for y_ in ys:
            Y_appeared[y_] = True
for x, y in XY:
    if X_appeared[x] or Y_appeared[y]:
        continue
    cnt += 1
print(cnt-N)
