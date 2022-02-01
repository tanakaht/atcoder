import sys

input = sys.stdin.readline
N = int(input())
K = int(input())
is_white = [list(map(lambda x: x=='.', input())) for _ in range(N)]
ans = 0
for h in range(N):
    for w in range(N):
        if not is_white[h][w]:
            continue
        q = set([tuple([h*N+w])])
        for _ in range(K-1):
            new_q = set()
            for eles in q:
                for ele in eles:
                    h_, w_ = ele//N, ele%N
                    for dh, dw in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        h__, w__ = h_+dh, w_+dw
                        if 0<=h__<N and 0<=w__<N and is_white[h__][w__] and (h__*N+w__ not in eles):
                            tmp = list(eles)+[h__*N+w__]
                            new_q.add(tuple(e for e in sorted(tmp)))
            q = new_q
        ans += len(q)
        is_white[h][w] = 0
print(ans)
