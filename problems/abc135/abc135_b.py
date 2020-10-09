N = int(input())
p = list(map(int, input().split()))
cnt = 0
for i, a in enumerate(p):
    cnt += (i + 1) != a

print('YES' if cnt <= 2 else 'NO')
