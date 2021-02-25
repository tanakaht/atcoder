from collections import Counter
H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
for h in range(H-1):
    for w in range(W-1):
        c = Counter(S[h][w:w+2]+S[h+1][w:w+2])
        ans += c['#']==1 or c['.']==1
print(ans)
