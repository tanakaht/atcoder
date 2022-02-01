import sys
N, Q = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(Q)]
cant_use = [set([i]) for i in range(N)]
for x, y in XY:
    x -= 1
    y -= 1
    cant_use[x].add(y)
    cant_use[y].add(x)
available = [None]*8889
available[0] = set()
for i in range(N):
    s = cant_use[i]
    for v in range(8889-A[i]):
        if available[v] is not None and (not s.intersection(available[v])):
            new_set = set([x for x in available[v]])
            new_set.add(i)
            if available[v+A[i]] is not None:
                print(len(available[v+A[i]]))
                print(*[x+1 for x in available[v+A[i]]])
                print(len(new_set))
                print(*[x+1 for x in new_set])
                sys.exit(0)
            else:
                available[v+A[i]] = new_set
raise ValueError
