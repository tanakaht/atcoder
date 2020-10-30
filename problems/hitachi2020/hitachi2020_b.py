A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
xyc = [list(map(int, input().split())) for _ in range(M)]
ans_kouho = [min(a)+min(b)] + [a[x-1]+b[y-1]-c for x, y, c in xyc]
print(min(ans_kouho))

