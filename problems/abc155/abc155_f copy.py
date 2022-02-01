import sys

input = sys.stdin.readline
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
LR = [list(map(int, input().split())) for _ in range(M)]
events = []
for a, b in AB:
    events.append((a, b, 'N'))
for i, (l, r) in enumerate(LR):
    events.append((l-1/2, i, 'L'))
    events.append((r+1/2, i, 'R'))

events = sorted(events, key=lambda x: x[0])
edges = [[None, None] for _ in range(M)]
status  = [0]*(N+1)
cnt = 0
pre_status = 0
for x, v, flg in events:
    if flg == 'N':
        status[cnt] = v^pre_status
        pre_status = v
        cnt += 1
    if flg == 'L':
        edges[v][0] = cnt
    if flg == 'R':
        edges[v][1] = cnt

status[cnt] = sum(status)%2
g=[[] for _ in range(N+1)]
for i, (a, b) in enumerate(edges):
    g[a].append((b, i))
    g[b].append((a, i))

is_used = [0]*M
appeared, withdrawed = [False]*(N+1), [False]*(N+1)
added = [False]*(N+1)
for start_node in range(N+1):
    if appeared[start_node]:
        continue
    q = [(~start_node, None), (start_node, None)]
    is_toru = False
    while q:
        u, i = q.pop()
        if u >= 0:
            if appeared[u]:
                continue
            appeared[u] = True
            # 入った時の処理
            if is_toru:
                is_used[i] ^= 1
            is_toru ^= status[u]
            # 探索先を追加
            for v, i in g[u][::-1]:
                if added[v]:
                    continue
                q.append((~v, i))
                q.append((v, i))
        else:
            if withdrawed[~u]:
                continue
            withdrawed[~u] = True
            # 出た時の処理
            if is_toru and not i is None:
                is_used[i] ^= 1
    if is_toru:
        print(-1)
        sys.exit(0)
ans = []
for i in range(M):
    if is_used[i]:
        ans.append(i+1)
print(len(ans))
print(*ans)
