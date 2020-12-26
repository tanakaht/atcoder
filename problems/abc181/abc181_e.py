from bisect import bisect
import math

N, M = map(int, input().split())
H = sorted(list(map(int, input().split())))
W = sorted(list(map(int, input().split())))
C_left = [0]  # 左から2*i番目まで左から組む
C_right = [0]  # 右から2*j番目まで右から組む
for i in range(N // 2):
    C_left.append(C_left[-1]+abs(H[2*i]-H[2*i+1]))
    C_right.append(C_right[-1]+abs(H[-2*i-1]-H[-2*i-2]))

ans = math.inf
for w in W:
    idx = bisect(H, w)
    l = idx // 2
    r = N // 2 - l
    aite = H[idx] if idx%2==0 else H[idx-1]
    ans = min(ans, C_left[l] + C_right[r] + abs(w - aite))
print(ans)
