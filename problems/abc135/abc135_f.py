import math
import sys

sys.setrecursionlimit(int(1e7))

def z_algorithm(S):
    N = len(S)
    Z_arr = [0] * N
    Z_arr[0] = N
    i = 1
    j = 0
    while i < N:
        while i+j < N and S[j] == S[i+j]:
            j += 1
        Z_arr[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < N and k + Z_arr[k] < j:
            Z_arr[i+k] = Z_arr[k]
            k += 1
        i += k
        j -= k
    return Z_arr


s = input()
t = input()
start_pos = [False]*len(s)
z_arr = z_algorithm(t+'$'+s*(len(t)//len(s)+2))
for i in range(len(t)+1, len(z_arr)):
    if z_arr[i]==len(t):
        start_pos[(i-len(t)-1)%len(s)] = True
lcs_len = [None] * len(s)
appeared = [False] * len(s)
def solve(i):
    if lcs_len[i] is not None:
        return lcs_len[i]
    if lcs_len[i] is None and appeared[i]:
        return math.inf
    if not start_pos[i]:
        appeared[i] = True
        lcs_len[i] = 0
        return 0
    appeared[i] = True
    l = solve((i+len(t))%len(s))+1
    lcs_len[i] = l
    return l

ans = 0
for i in range(len(s)):
    ans = max(ans, solve(i))
if ans == math.inf:
    print(-1)
else:
    print(ans)
