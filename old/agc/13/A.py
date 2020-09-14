N = int(input())
A = list(map(int, input().split()))

flg = 0
i = 0
cnt = 1
pre = None
for a in A:
    if pre is None:
        pre = a
    if flg * (a-pre) < 0:
        flg = 0
        cnt += 1
        pre = None
    else:
        flg = a-pre
        pre = a

print(cnt)
