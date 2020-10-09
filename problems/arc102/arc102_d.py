import sys

input = sys.stdin.readline
N = int(input())
p = [int(input()) for _ in range(N)]
p_tmp = [i for i in p]
swap_idx = []
i = 0
while i < N:
    if p_tmp[i] == i + 1:
        i += 1
        continue
    found = False
    for j in range(i + 2, N, 2):
        if p_tmp[j] == i + 1:
            found = True
            break
    if not found:
        print('No')
        sys.exit(0)
    # checkいるかも？
    # swap
    tmp = p_tmp[j]
    for k in range(j, i, -2):
        p_tmp[k] = p_tmp[k - 2]
    p_tmp[i] = tmp
    for k in range(i+1, j, 2):
        if p_tmp[k] != k + 1:
            print('No')
            sys.exit(0)
    i += 2
print('Yes')
