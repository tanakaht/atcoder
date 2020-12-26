from collections import defaultdict, deque
import sys

H, W = map(int, input().split())
M = ['#' * (W + 2)] + ['#' + input() + '#' for _ in range(H)] + ['#' * (W + 2)]
alpha = defaultdict(lambda: [])
for h in range(H+2):
    for w in range(W+2):
        if M[h][w] == 'S':
            s = (h, w)
        elif M[h][w] == 'G':
            g = (h, w)
        elif M[h][w] == '.':
            pass
        elif M[h][w] == '#':
            pass
        else:
            alpha[M[h][w]].append((h, w))
q = deque([(0, s[0], s[1])])
visited = [[False]*(W+2) for _ in range(H+2)]
use_alpha = set([])
while q:
    t, h, w = q.popleft()
    if h == g[0] and w == g[1]:
        print(t)
        sys.exit()
    for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        h_, w_ = h + d[0], w + d[1]
        if visited[h_][w_]:
            continue
        elif M[h_][w_] != '#':
            q.append((t + 1, h_, w_))
            visited[h_][w_] = True
        if M[h][w] not in use_alpha:
            for h_, w_ in alpha[M[h][w]]:
                q.append((t + 1, h_, w_))
            use_alpha.add(M[h][w])
print(-1)
