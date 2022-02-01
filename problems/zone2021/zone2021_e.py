import heapq, math

R, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
B = [list(map(int, input().split())) for _ in range(R-1)]
g = [[] for _ in range(R*C*2)] # (1+iの1を支払った)*RC+r*C+c
for r in range(R):
    for c in range(C):
        # 払ってない
        u = r*C+c
        if c+1<C:
            v = r*C+c+1
            g[u].append((v, A[r][c]))
        if c-1>=0:
            v = r*C+c-1
            g[u].append((v, A[r][c-1]))
        if r+1<R:
            v = (r+1)*C+c
            g[u].append((v, B[r][c]))
        v = R*C+r*C+c
        g[u].append((v, 1))

        # 払った
        u = R*C+r*C+c
        if r-1>=0:
            v = R*C+(r-1)*C+c
            g[u].append((v, 1))
        v = r*C+c
        g[u].append((v, 0))

q = [(0, 0)]
dist = [math.inf]*(R*C*2)
appeared = [False]*(R*C*2)
while q:
    d, u = heapq.heappop(q)
    if appeared[u]:
        continue
    appeared[u] = True
    dist[u] = d
    if u == R*C-1:
        break
    for v, d_ in g[u]:
        if appeared[v] or dist[v]<=d+d_:
            continue
        heapq.heappush(q, (d+d_, v))
        dist[v] = d+d_
print(dist[R*C-1])
