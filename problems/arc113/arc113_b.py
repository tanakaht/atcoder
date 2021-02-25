A, B, C = map(int, input().split())
d = {}
a = A%10
tmp = 1
for i in range(11):
    if tmp in d.values():
        for loop_start in range(i):
            if d[loop_start] == tmp:
                break
        loop_len = i - loop_start
        break
    d[i] = tmp
    tmp = (tmp*a)%10
idx = (pow(B, C, loop_len*11) - loop_start) % loop_len + loop_start
ans = d[idx]
print(ans)
