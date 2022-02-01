import sys

sys.setrecursionlimit(int(1e6))

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
g = [[] for _ in range(N)]
for a, b in AB:
    g[a-1].append(b-1)
    g[b - 1].append(a - 1)

ans = 0
t_in_cnt, t_out_cnt = [None]*N, [None]*N
appeared, withdrawed = [False]*N, [False]*N
start_node = 0
q = [~start_node, start_node]
withdraw_cnt = 0
while q:
    u = q.pop()
    if u >= 0:
        if appeared[u]:
            continue
        appeared[u] = True
        # 入った時の処理
        # 記録
        t_in_cnt[u] = withdraw_cnt
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
        # 記録
        withdraw_cnt += 1
        t_out_cnt[~u] = withdraw_cnt
        # 出た時の処理
        cnt = t_out_cnt[~u]-t_in_cnt[~u]
        ans += cnt*(N-cnt)
print(ans)
