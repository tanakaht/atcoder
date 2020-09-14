N, K = map(int, input().split())
H = sorted(list(map(int, input().split())))
if K == 0:
    print(sum(H))
else:
    print(sum(H[:-K]))
