import sys

input = sys.stdin.readline
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
g = [[]for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

def farest(start_node):
    appeared, withdrawed = [False]*N, [False]*N
    ret = (0, start_node)
    d = 0
    q = [~start_node, start_node]
    while q:
        u = q.pop()
        if u >= 0:
            if appeared[u]:
                continue
            appeared[u] = True
            # 入った時の処理
            d += 1
            if ret[0] < d:
                ret = (d, u)
            # 探索先を追加
            for v in g[u][::-1]:
                if appeared[v]:
                    continue
                q.append(~v)
                q.append(v)
        else:
            if withdrawed[~u]:
                continue
            withdrawed[~u] = True
            # 出た時の処理
            d -= 1
            # 記録
    return ret

p1 = farest(0)
p2 = farest(p1[1])
print(p2[0])
