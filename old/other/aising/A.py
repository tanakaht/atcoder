L, R, D = map(int, input().split())
cnt = 0
for i in range(L, R+1):
    if i % D == 0:
        cnt += 1
print(cnt)