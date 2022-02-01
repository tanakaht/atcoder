import sys

N = input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
gs = [[[] for _ in range(51)] for _ in range(51)]
for k in range(1, 51):
    for i in range(1, 51):
        if i%k!=i:
            gs[k][i].append(i%k)


def canreach(gs, n):
    ret = set()
    g = [set() for _ in range(51)]
    for g_ in gs:
        for i in range(51):
            for j in g_[i]:
                g[i].add(j)
    q = [n]
    ret.add(n)
    while q:
        u = q.pop()
        for v in g[u]:
            if v in ret:
                continue
            ret.add(v)
            q.append(v)
    return ret

def is_ok(gs, hastoreach):
    for i in range(51):
        S = canreach(gs, i)
        for j in hastoreach[i]:
            if j not in S:
                return False
    return True

hastoreach = [set() for _ in range(51)]
for a, b in zip(A, B):
    if a!= b:
        hastoreach[a].add(b)

if not is_ok(gs, hastoreach):
    print(-1)
    sys.exit(0)

ans = 0
for k in range(50, -1, -1):
    if is_ok(gs[:k]+gs[k+1:], hastoreach):
        gs[k] = [[] for _ in range(51)]
    else:
        ans += 1<<k
print(ans)
