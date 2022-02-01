N = int(input())
A, B, C = map(int, input().split())
ans = 10000
for a in range(10001):
    for b in range(10001):
        if A*a+B*b>N:
            break
        if (N-A*a-B*b)%C==0:
            c = (N-A*a-B*b)//C
            ans = min(ans, a+b+c)
print(ans)
