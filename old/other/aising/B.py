N = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i, a in enumerate(A):
    ans += (i+1)%2==1 and a%2==1
print(ans)